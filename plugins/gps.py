from userge import userge, Message
from geopy.geocoders import Nominatim


@userge.on_cmd("gps", about={
    'header': "locate the coordinates of addresses, cities, countries, and landmarks",
    'usage': "{tr}gps [location]\ne.g {tr}gps 175 5th Avenue NYC"})
async def gps_locate_(message: Message):
    loc_ = message.input_str
    if not loc_:
        return await message.err('Provide a valid location name', del_in=5)
    await message.edit("Finding This Location In Maps Server.....")
    geolocator = Nominatim(user_agent="USERGE-X")
    geoloc = geolocator.geocode(loc_)
    if not geoloc:
        return await message.err('404: Not Found', del_in=5)
    title = geoloc.point
    address = geoloc.address
    place = address.split(",")
    lon = geoloc.longitude
    lat = geoloc.latitude
    await message.delete()
    await message.client.send_venue(
        message.chat.id, 
        lat, 
        lon,
        place[0], 
        address
    )