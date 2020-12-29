import string
import random
import discord
import random
from discord.ext import commands

SMBIOS = {
    "macbookair9,1":    "**Name**: MacBookAir9,1 \n**Serial**: FVF{SERIAL}MNHP \n**MLB**: FVF{MLB1}0000{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macbookpro11,1":   "**Name**: MacBookPro11,1 \n**Serial**: C02{SERIAL}FH00 \n**MLB**: C02{MLB1}FH31{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macbookpro11,2":   "**Name**: MacBookPro11,2 \n**Serial**: C02{SERIAL}G86R \n**MLB**: C02{MLB1}FJQW{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macbookpro11,3":   "**Name**: MacBookPro11,3 \n**Serial**: C02{SERIAL}FR1M \n**MLB**: C02{MLB1}FP52{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macbookpro11,4":   "**Name**: MacBookPro11,4 \n**Serial**: C02{SERIAL}G8WN \n**MLB**: C02{MLB1}DQP1{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macbookpro11,5":   "**Name**: MacBookPro11,5 \n**Serial**: C02{SERIAL}G85Y \n**MLB**: C02{MLB1}GF2C{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macbookpro12,1":   "**Name**: MacBookPro12,1 \n**Serial**: C02{SERIAL}H1DP \n**MLB**: C02{MLB1}GDVV{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macbookpro13,1":   "**Name**: MacBookPro13,1 \n**Serial**: C17{SERIAL}GVC1 \n**MLB**: C17{MLB1}HMHK{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macbookpro13,2":   "**Name**: MacBookPro13,2 \n**Serial**: C02{SERIAL}GYFH \n**MLB**: C02{MLB1}H9W8{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macbookpro13,3":   "**Name**: MacBookPro13,3 \n**Serial**: C02{SERIAL}GTFN \n**MLB**: C02{MLB1}HCF9{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macbookpro14,1":   "**Name**: MacBookPro14,1 \n**Serial**: C02{SERIAL}HV29 \n**MLB**: C02{MLB1}HWVP{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macbookpro14,2":   "**Name**: MacBookPro14,2 \n**Serial**: C02{SERIAL}HV2N \n**MLB**: C02{MLB1}HRPC{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macbookpro14,3":   "**Name**: MacBookPro14,3 \n**Serial**: C02{SERIAL}HTD5 \n**MLB**: C02{MLB1}J1JH{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macbookpro15,1":   "**Name**: MacBookPro15,1 \n**Serial**: C02{SERIAL}KGYG \n**MLB**: C02{MLB1}JP4F{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macbookpro15,2":   "**Name**: MacBookPro15,2 \n**Serial**: C02{SERIAL}JHCC \n**MLB**: C02{MLB1}JH4R{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macbookpro15,3":   "**Name**: MacBookPro15,3 \n**Serial**: C02{SERIAL}LVCG \n**MLB**: C02{MLB1}0000{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macbookpro15,4":   "**Name**: MacBookPro15,4 \n**Serial**: FVF{SERIAL}L40Y \n**MLB**: FVF{MLB1}0000{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macbookpro16,1":   "**Name**: MacBookPro16,1 \n**Serial**: C02{SERIAL}MD6N \n**MLB**: C02{MLB1}N9PR{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macbookpro16,2":   "**Name**: MacBookPro16,2 \n**Serial**: C02{SERIAL}ML7H \n**MLB**: C02{MLB1}0000{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macbookpro16,3":   "**Name**: MacBookPro16,3 \n**Serial**: C02{SERIAL}P3XY \n**MLB**: C02{MLB1}0000{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macbookpro16,4":   "**Name**: MacBookPro16,4 \n**Serial**: C02{SERIAL}MD6T \n**MLB**: C02{MLB1}0000{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macmini7,1":       "**Name**: Macmini7,1 \n**Serial**: C02{SERIAL}G1J0 \n**MLB**: C02{MLB1}G0MC{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macmini8,1":       "**Name**: Macmini8,1 \n**Serial**: C07{SERIAL}JYVX \n**MLB**: C07{MLB1}KXPG{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "imac14,1":         "**Name**: iMac14,1 \n**Serial**: D25{SERIAL}FWJH \n**MLB**: D25{MLB1}FM59{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "imac14,2":         "**Name**: iMac14,2 \n**Serial**: D25{SERIAL}F8JC \n**MLB**: D25{MLB1}F8YL{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "imac14,3":         "**Name**: iMac14,3 \n**Serial**: D25{SERIAL}FWJH \n**MLB**: D25{MLB1}F9RR{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "imac14,4":         "**Name**: iMac14,4 \n**Serial**: D25{SERIAL}FY0T \n**MLB**: D25{MLB1}G36D{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "imac15,1":         "**Name**: iMac15,1 \n**Serial**: C02{SERIAL}FY10 \n**MLB**: C02{MLB1}G2Y7{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "imac16,1":         "**Name**: iMac16,1 \n**Serial**: D25{SERIAL}GF1J \n**MLB**: D25{MLB1}GH34{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "imac16,2":         "**Name**: iMac16,2 \n**Serial**: DGK{SERIAL}GG7F \n**MLB**: DGK{MLB1}GQRY{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "imac17,1":         "**Name**: iMac17,1 \n**Serial**: C02{SERIAL}GG7L \n**MLB**: C02{MLB1}GPF7{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "imac18,1":         "**Name**: iMac18,1 \n**Serial**: C02{SERIAL}H7JY \n**MLB**: C02{MLB1}H69F{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "imac18,2":         "**Name**: iMac18,2 \n**Serial**: C02{SERIAL}J1G5 \n**MLB**: C02{MLB1}J0DX{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "imac18,3":         "**Name**: iMac18,1 \n**Serial**: C02{SERIAL}J1GJ \n**MLB**: C02{MLB1}J0PG{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "imac19,1":         "**Name**: iMac19,1 \n**Serial**: C02{SERIAL}JV3Q \n**MLB**: C02{MLB1}LNV9{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "imac19,2":         "**Name**: iMac19,1 \n**Serial**: C02{SERIAL}JWDW \n**MLB**: C02{MLB1}KGQG{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "imac20,1":         "**Name**: iMac20,1 \n**Serial**: C02{SERIAL}PN5T \n**MLB**: C02{MLB1}PHCD{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "imac20,2":         "**Name**: iMac20,1 \n**Serial**: C02{SERIAL}046M \n**MLB**: C02{MLB1}0000{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "imacpro1,1":       "**Name**: iMacPro1,1 \n**Serial**: C02{SERIAL}HX87 \n**MLB**: C02{MLB1}JG36{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macpro6,1":        "**Name**: MacPro6,1 \n**Serial**: F5K{SERIAL}F9VM \n**MLB**: F5K{MLB1}FHDD{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
    "macpro7,1":        "**Name**: MacPro7,1 \n**Serial**: F5K{SERIAL}P7QM \n**MLB**: F5K{MLB1}K3F7{MLB2} \n**UUID**: {UUID1}-{UUID2}-4{UUID3}-{UUID4}-{UUID5}",
}

class gen_smbios(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    async def get_random(self, num:int):
        a = random.choices(string.ascii_uppercase + string.digits, k=num)
        string_random = ' '.join(map(str, a)).replace(" ", "")
        return string_random

    @commands.command()
    async def gen(self, ctx, name):
        get_smbios = SMBIOS.get(name.lower().strip())
        if not get_smbios:
            await ctx.send(f"Can not find SMBIOS with {name}")

        result = get_smbios.format(
            SERIAL = await self.get_random(5),
            MLB1 = await self.get_random(8),
            MLB2 = await self.get_random(2),
            UUID1 = await self.get_random(8),
            UUID2 = await self.get_random(4),
            UUID3 = await self.get_random(3),
            UUID4 = await self.get_random(4),
            UUID5 = await self.get_random(12)
            )
        embed = discord.Embed(colour=discord.Colour.dark_orange())
        embed.add_field(name = "SMBIOS Information:", value = result, inline=False)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(gen_smbios(bot))