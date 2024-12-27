from aiohttp import web
from config import *

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("LazyDeveloperr")


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app




# from aiohttp import web
# from plugins.renderapi import render_lazydeveloper
# from config import *
# import logging

# routes = web.RouteTableDef()

# # Root route to check if the server is up
# @routes.get("/", allow_head=True)
# async def root_route_handler(request):
#     return web.json_response({"message": "LazyDeveloper API is up!"})

# # This route fetches information from the API (file details) based on the short URL
# @routes.get(r"/api/get-info?shorturl={key}", allow_head=True)
# async def get_info_handler(request: web.Request):
#     try:
#         shorturl = request.match_info["key"]
#         # pwd = request.query.get('pwd', '')  # password (optional)

#         if not shorturl:
#             return web.json_response({"ok": False, "message": "shorturl is required!"})

#         # Render the page to get file info (you can adjust this to your needs)
#         final_info = await render_lazydeveloper(shorturl)

#         return web.json_response({"ok": True, "message": "Fetched file info", "data": final_info})

#     except Exception as e:
#         logging.error(e, exc_info=True)
#         return web.json_response({"ok": False, "message": f"❌ An error occurred: {str(e)}"})



# # This route fetches the download link after we have file details
# @routes.get(r"/api/get-download", allow_head=True)
# async def get_download_handler(request: web.Request):
#     try:
#         # Use query params to extract the necessary info
#         shareid = request.query.get('shareid')
#         uk = request.query.get('uk')
#         sign = request.query.get('sign')
#         timestamp = request.query.get('timestamp')
#         fs_id = request.query.get('fs_id')

#         if not all([shareid, uk, sign, timestamp, fs_id]):
#             return web.json_response({"ok": False, "message": "Missing required parameters!"})

#         # Fetch the download link here (implement your logic to fetch download URL)
#         download_link = await fetch_download_link(shareid, uk, sign, timestamp, fs_id)

#         return web.json_response({"ok": True, "download_link": download_link})

#     except Exception as e:
#         logging.error(e, exc_info=True)
#         return web.json_response({"ok": False, "message": f"❌ An error occurred: {str(e)}"})

# async def fetch_download_link(shareid, uk, sign, timestamp, fs_id):
    # Implement the logic to fetch the actual download link
    # Example:
    # Call an external API or your internal logic to get the actual link
    #return "http://example.com/download_link"



# @routes.get(r"/api/get-info?shorturl={shortUrl}", allow_head=True)
# async def play_handler(request: web.Request):
#     try:
#         # got_info = request.match_info["params"]
#         # Render the play.html with the retrieved URL
#         # final_info = f"api/{got_info}"
        
#         shorturl = request.query.get("shorturl")

#         print(f"here i shorturl ->  {shorturl}")
#         return web.Response(
#             text=await render_lazydeveloper(shorturl),
#             content_type="text/html"
#         )

#     except Exception as e:
#         logging.critical(e, exc_info=True)
#         raise web.HTTPInternalServerError(text=f"❌ An error occurred: {str(e)}")


# @routes.get("/api/get-info")
# async def get_info_handler(request: web.Request):
    # """
    # Handles requests to fetch file info from TeraBox using the short_url.
    # """
    # short_url = request.query.get("shorturl")
    # password = request.query.get("pwd", "")

    # if not short_url:
    #     return web.json_response({"ok": False, "message": "shorturl parameter is required"}, status=400)

    # try:
    #     # Simulate fetching file info (you can replace this with real logic)
    #     file_info = {
    #         "ok": True,
    #         "shareid": "example_shareid",
    #         "uk": "example_uk",
    #         "sign": "example_sign",
    #         "timestamp": 1234567890,
    #         "list": [
    #             {
    #                 "filename": "example.mp4",
    #                 "size": 123456789,
    #                 "fs_id": "example_fs_id",
    #                 "is_dir": 0
    #             }
    #         ]
    #     }
    #     return web.json_response(file_info)
    # except Exception as e:
    #     logging.critical(f"Error in get-info: {e}")
    #     return web.json_response({"ok": False, "message": str(e)}, status=500)