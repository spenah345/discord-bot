import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} sudah aktif!')

@bot.command()
async def gaji(ctx):
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    await ctx.send("Masukkan Nama:")
    nama = await bot.wait_for("message", check=check)

    await ctx.send("Masukkan Posisi:")
    posisi = await bot.wait_for("message", check=check)

    await ctx.send("Masukkan Total Pengeluaran Seminggu (angka saja):")
    pengeluaran = await bot.wait_for("message", check=check)

    try:
        total = float(pengeluaran.content)
        pembagian = total * 0.5
        hasil = f"""```
Nama: {nama.content}
Posisi: {posisi.content}
Salary: Rp{pembagian:,.0f}
```"""
        await ctx.send(hasil)
    except ValueError:
        await ctx.send("Input pengeluaran harus berupa angka!")

# Ambil token dari environment variable (cocok untuk Railway)
token = os.getenv("MTM2MDExODM3NTg2NjU2NDY2OA.GMekwA.tdcxWJ_eGAo-5Q0_XjQEyMcynDeB3nkeCmPffc")
bot.run(token)
