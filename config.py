from dotenv import dotenv_values
ENV = dotenv_values('.env')
token = ENV['TOKEN']
print(token)
