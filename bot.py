import discord
import discord
from discord.ext import commands

client = discord.Client()

class chatbot(discord.Client):
    
    async def on_ready(self):
       
        game = discord.Game("주인병신ㅋㅋㅋㅋㅋㅋㅋ")

        
        await client.change_presence(status=discord.Status.online, activity=game)

       
        print("작동준비 완료!")

    
    async def on_message(self, message):
       
        if message.author.bot:
            return None
        
 
        if message.content == "현타야 하이":
            channel = message.channel
            
            msg = "하2"

            await channel.send(msg)
            return None

        if message.content == "현타야 현재 사용 언어":
            channel = message.channel
            
            msg = "이건 파이썬!"
            
            await channel.send(msg)
            return None

        if message.content == "현타야":
            channel = message.channel
            
            msg = "왜!"
            
            await channel.send(msg)
            return None

        if message.content == "현타야 도움말":
            
            channel = message.channel
            
            msg = "없음 ㅅㄱ ㅋㅋㅋㅋㅋㅋㅋ"
            
            await channel.send(msg)
            return None

        if message.content == "현타야 현타온다":
            
            channel = message.channel
            
            msg = "그려서ㅍㅋㅍㅋ"
            
            await channel.send(msg)
            return None
       
        if message.content == "현타야 맨션":
            channel = message.channel

            msg = "<@{}> 이제 만족했냐?".format(message.author.id)
            await channel.send(msg)
            return None
        
        if message.content == "현타야 자폭해":
            
            channel = message.channel
            
            msg = "500만원을 입금하시면 자폭이 진행됩니다."
            
            await channel.send(msg)
            return None

        if message.content == "현타야 폭8":
            
            channel = message.channel
            
            msg = "폭8은 언제나 짜릿해!"
            
            await channel.send(msg)
            return None

        if message.content == "현타야 닥처":
            
            channel = message.channel
            await message.channel.send("<@{}> 너나 닥치세요 이 개쓰레기 새끼야.".format(message.author.id))
            await message.channel.purge(limit=1)
              
        if message.content == "[ping]" :
          commander = discord.utils.get(message.guild.roles, name="서버 업뎃")
          await message.channel.send("{} ^^".format(commander.mention))

        if message.content == "[PING]" :
          commander = discord.utils.get(message.guild.roles, name="서버 업뎃")
          await message.channel.send("{} ^^".format(commander.mention))

        if message.content == "||[ping]||" :
          commander = discord.utils.get(message.guild.roles, name="서버 업뎃")
          await message.channel.send("{} ^^".format(commander.mention))

        if message.content == "||[PING]||" :
          commander = discord.utils.get(message.guild.roles, name="서버 업뎃")
          await message.channel.send("{} ^^".format(commander.mention))
        
        if message.content == "[ㅔㅑㅜㅎ]" :
          commander = discord.utils.get(message.guild.roles, name="서버 업뎃")
          await message.channel.send("{} ^^".format(commander.mention))
        
        if message.content == "||[ㅔㅑㅜㅎ]||" :
          commander = discord.utils.get(message.guild.roles, name="서버 업뎃")
          await message.channel.send("{} ^^".format(commander.mention))






        if message.content == "!서버 열림":
          await message.channel.purge(limit=1)
          channel = message.channel
        
          embed = discord.Embed(title="서버 상태", description="Open", color=0X53FF4C)

          embed.add_field(name="호스트", value="Lagging Computer", inline=True)

          await channel.send(embed=embed)

          commander = discord.utils.get(message.guild.roles, name="서버 업뎃")
          await message.channel.send("{} 서버가 열렸습니다.".format(commander.mention))

        if message.content == "!서버 오류":
          await message.channel.purge(limit=1)
          channel = message.channel

          embed=discord.Embed(title="현재 서버 상황", url="https://cdn.discordapp.com/attachments/811591823632891934/811592202744496198/png-transparent-check-mark-computer-icons-icon-design-complete-angle-logo-grass.png", description="버그발생", color=0xfff612)
         
          embed.set_author(name="서버 에러 발생", icon_url="https://cdn.discordapp.com/attachments/811591823632891934/811591843690971176/223008431047.jpg")
         
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/811591823632891934/811591843690971176/223008431047.jpg")
         
          embed.add_field(name="서버 현황", value="고치고 있는중", inline=False)
          
          await channel.send(embed=embed)

          commander = discord.utils.get(message.guild.roles, name="서버 업뎃")
          await message.channel.send("{} 서버긴급 오류가 발생하였습니다..".format(commander.mention))

        if message.content == "!서버 복구":
          await message.channel.purge(limit=1)

          embed=discord.Embed(title="서버 상황", description="정상작동", color=0x2fed28)

          embed.set_author(name="서버 복구", icon_url="https://cdn.discordapp.com/attachments/811591823632891934/811592202744496198/png-transparent-check-mark-computer-icons-icon-design-complete-angle-logo-grass.png")
          
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/811591823632891934/811592202744496198/png-transparent-check-mark-computer-icons-icon-design-complete-angle-logo-grass.png")
          
          embed.add_field(name="복구 완료", value="정상작동 중", inline=False)
          
          embed.add_field(name="서버 호스트", value="레깅", inline=True)
          
          await channel.send(embed=embed)

          commander = discord.utils.get(message.guild.roles, name="서버 업뎃")
          await message.channel.send("{} 서버복구가 되었습니다.".format(commander.mention))

        if message.content == "!서버 종료":
          await message.channel.purge(limit=1)
          channel = message.channel
          embed = discord.Embed(title="서버 상태", description="Close", color=0XED0000)

          embed.add_field(name="재 오픈", value="내일 오전때", inline=True)

          await channel.send(embed=embed)

          commander = discord.utils.get(message.guild.roles, name="서버 업뎃")
          await message.channel.send("{} 서버가 닫혀있습니다.".format(commander.mention))

        if message.content == "현타야 주안타스 정보":
         channel = message.channel
        
         embed = discord.Embed(title="회사이름 및 기업정보", description="회사이름:주안타스교통공사\n\n 기업정보:공기업", color=0x00ff56)

         embed.add_field(name="사원이름", value="회장:hyunta_2301\n\n 사장:tas_2031\n\n 부사장:주안\n\n 전무:현타\n\n 부장:Modeler_Flip,화곡\n\n 사원:dh", inline=True)

    
         await channel.send(embed=embed)

        if message.content == "현타야 레이컨 정보":
         channel = message.channel
        
         embed = discord.Embed(title="회사이름 및 기업정보", description="회사이름:레이컨레일\n\n 기업정보:사기업", color=0x00ff56)

         embed.add_field(name="사원이름", value="회장:\n\n 사장:\n\n 부사장:\n\n 전무:\n\n 부장:\n\n 사원:", inline=True)

    
         await channel.send(embed=embed)

        if message.content == "ㅗ":
          await message.channel.purge(limit=1)
          await message.channel.send("<@{}> 어허 그건 안돼~".format(message.author.id))
         
          await message.channel.purge(limit=1)

        if message.content == "현타야 ㅗ":
          await message.channel.purge(limit=1)
          await message.channel.send("<@{}> 어허 그건 안돼~".format(message.author.id))
          
        
        if message.content == "fuck":
          await message.channel.purge(limit=1)
          await message.channel.send("<@{}> Oh~ no~".format(message.author.id))
          

        if message.content == "그게 뭔데요":
            
            channel = message.channel
            msg = "ㅇㅈ 그게 뭔데요"

            await channel.send(msg)
            return None

        if message.content == "그게 뭔데":
            
            channel = message.channel
            msg = "ㅇㅈ 그게 뭔데"

            await channel.send(msg)
            return None

        if message.content == "ㅇㅈ?":
            
            channel = message.channel
            msg = "ㅇㅇㅈ"

            await channel.send(msg)
            return None

        if message.content == "어의가 없네":
            
            channel = message.channel
            msg = "아 진짜 어의가 없넼ㅋㅋㅋㅋㅋㅋㅋ"

            await channel.send(msg)
            return None

        if message.content == "이예":
            
            channel = message.channel
            msg = "저녀석 왜 이렇게 신난거여?"

            await channel.send(msg)
            return None


if __name__ == "__main__":
    
    client = chatbot()


client.run(os.environ['token'])