# corona virus status
from covid import Covid

from ..utils import admin_cmd, edit_or_reply
from . import CMD_HELP


@borg.on(admin_cmd(pattern="covid(?: |$)(.*)"))
async def corona(event):
    if event.pattern_match.group(1):
        country = (event.pattern_match.group(1)).title()
    else:
        country = "World"
    event = await edit_or_reply(event, "`collecting data...........`")
    covid = Covid(source="worldometers")
    try:
        country_data = covid.get_status_by_country_name(country)
    except ValueError:
        country_data = ""
    if country_data:
        hmm1 = country_data["confirmed"] + country_data["new_cases"]
        hmm2 = country_data["deaths"] + country_data["new_deaths"]
        data = ""
        data += f"\n⚠️Confirmed   : <code>{hmm1}</code>"
        data += f"\n😔Active           : <code>{country_data['active']}</code>"
        data += f"\n⚰️Deaths         : <code>{hmm2}</code>"
        data += f"\n🤕Critical          : <code>{country_data['critical']}</code>"
        data += f"\n😊Recovered   : <code>{country_data['recovered']}</code>"
        data += f"\n💉Total tests    : <code>{country_data['total_tests']}</code>"
        data += f"\n🥺New Cases   : <code>{country_data['new_cases']}</code>"
        data += f"\n😟New Deaths : <code>{country_data['new_deaths']}</code>"
        await event.edit(
            "<b>Corona Virus Info of {}:\n{}</b>".format(country, data),
            parse_mode="html",
        )
    else:
        data = await covidindia(country)
        if data:
            pgl1 = int(data["new_positive"]) - int(data["positive"])
            pgl2 = int(data["new_death"]) - int(data["death"])
            pgl3 = int(data["new_cured"]) - int(data["cured"])
            result = f"<b>Corona virus info of {data['state_name']}\
                \n\n⚠️Confirmed   : <code>{data['new_positive']}</code>\
                \n😔Active           : <code>{data['new_active']}</code>\
                \n⚰️Deaths         : <code>{data['new_death']}</code>\
                \n😊Recovered   : <code>{data['new_cured']}</code>\
                \n🥺New Cases   : <code>{pgl1}</code>\
                \n😟New Deaths : <code>{pgl2}</code>\
                \n😃New cured  : <code>{pgl3}</code> </b>"
            await event.edit(result, parse_mode="html")
        else:
            await edit_delete(
                event,
                "`Corona Virus Info of {} is not avaiable or unable to fetch`".format(
                    country
                ),
                5,
            )


CMD_HELP.update(
    {
        "covid": "**Plugin : **`covid`\
        \n\n**Syntax : **`.covid <country name>`\
        \n**Function :** __Get an information about covid-19 data in the given country.__\
        \n\n**Syntax : **`.covid <state name>`\
        \n**Function :** __Get an information about covid-19 data in the given state of India only.__\
        "
    }
)
