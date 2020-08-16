from twilio.rest import Client 
 
account_sid = 'AC571204bbe1dcde882e77c4c1b3997532' 
auth_token = '616efad0be70f1233f91d611761e049d' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:+917686962350' 
                          ) 
 
print(message.sid)