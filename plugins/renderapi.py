
# from config import *
# import aiofiles
# from config import *
# import aiohttp

# async def render_lazydeveloper(api_url):
#     async with aiofiles.open('template/dl.html') as r:
#         async with aiohttp.ClientSession() as s:
#             async with s.get(lazydevelopersrc) as u:
#                 heading = 'Download {}'.format(file_data.file_name)
#                 file_size = humanbytes(int(u.headers.get('Content-Length')))
#                 html = (await r.read()) % (heading, file_data.file_name, lazydevelopersrc, file_size)
#     return html

# async def render_lazydeveloper(api_url):
#     """
#     Render an HTML page for the given api URL and [ get-info?shorturl= or get-download].
#     """
#     # Load the play.html template
#     print(f'got api url => {api_url}')
#     async with aiofiles.open("temp_api/index.html", mode="r") as r:
#         html_content = await r.read()

#     # heading = "poweredby@LazyDeveloper"
#     print(f"I'm about to serve api ==> {api_url}")
#     html = html_content
#     return html
