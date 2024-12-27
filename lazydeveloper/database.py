import motor.motor_asyncio
from config import DB_URL, DB_NAME

class Database:

    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.user
        self.admins = self.db.admins  # New collection for forwarded IDs


    def new_user(self, id):
        return dict(
            _id=int(id),                                   
            file_id=None,
            caption=None
        )

    async def add_user(self, id):
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return bool(user)

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        all_users = self.col.find({})
        return all_users

    async def delete_user(self, user_id):
        await self.col.delete_many({'_id': int(user_id)})
    
    async def set_thumbnail(self, id, file_id):
        await self.col.update_one({'_id': int(id)}, {'$set': {'file_id': file_id}})

    async def get_thumbnail(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('file_id', None)

    async def set_caption(self, id, caption):
        await self.col.update_one({'_id': int(id)}, {'$set': {'caption': caption}})

    async def get_caption(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('caption', None)
        
    async def set_forward(self, id, forward):
        print(forward)
        z = await self.col.update_one({'_id': int(id)}, {'$set': {'forward_id': forward}})
        print(z)
    async def get_forward(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('forward_id', None)
    
    async def set_lazy_target_chat_id(self, id, target_chat_id):
        z = await self.col.update_one({'_id': int(id)}, {'$set': {'lazy_target_chat_id': target_chat_id}})
        print(z)

    async def get_lazy_target_chat_id(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('lazy_target_chat_id', None)
# ====================================================================
#                   Admin ID Management
# ====================================================================
    async def get_admin_ids(self):
        """
        Fetch the list of all admin IDs stored in the database.
        Returns an empty list if no admin IDs exist.
        """
        record = await self.admins.find_one({"type": "admin_list"})
        return record.get("admin_ids", []) if record else []

    async def add_admin_id(self, admin_id):
        """
        Add an admin ID to the list. Avoids duplicates using $addToSet.
        """
        await self.admins.update_one(
            {"type": "admin_list"},
            {"$addToSet": {"admin_ids": admin_id}},  # Avoid duplicates
            upsert=True  # Create the document if it doesn't exist
        )

    async def remove_admin_id(self, admin_id):
        """
        Remove an admin ID from the list.
        """
        await self.admins.update_one(
            {"type": "admin_list"},
            {"$pull": {"admin_ids": admin_id}}  # Remove the admin ID
        )   
# ====================================================================
# ====================================================================

db = Database(DB_URL, DB_NAME)
