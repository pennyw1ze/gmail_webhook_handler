# **DESCRIPTION**
gmail_webhook_handler allows a developer to run a self-hosted server captures every email received on your gmail account and is able to **filter**, **redirect**, **discard** or even **tag** the email as read.  
This can be done **COMPLETELY FOR FREE**.  

## **HOW DOES IT WORKS** 🤌
A python server runs on your local machine, and connects to a web interface trough an **ngrok** link.  
Ngrok is an **open source free** web services that provides a web interface to allow developers to tunnel informations from the web to local environments and use webhooks without buying a domain or opening any port on your routher.  
The python server is able to capture every email and look into the content.  
When an email is received, gmail webhooks send and **update**.  
When an update reaches your server, it will check into your account for **the most recent unread email** and will download and decrypt that email.  
The email will then result as a read email.  

## **POSSIBLE APPLICATION** 💡
Use your creativity!
Some ideas:
- Filter email sent by paypal, extract the information regarding the sender and the amount of money, keep a local balance of your expense, make your statistics, keep track of the money spent or earned, ecc. (There is a fun application to split Netflix and Spotify payment between friends via telegram bot that implements this webhook handler available on my github [here](https://github.com/pennyw1ze/paypal_splitter);
- Automatically download attachments from specific senders or with specific keywords in the subject
- Redirect just important emails by filtering the sender on your telegram account or a prioritary email ecc.;
- Personalized spam filter;
and a lot more!

---

# **HOW TO USE** 🚀
1. Clone the repository;
2. Install the requirements;
3. Set up the webhook on your gmail account;
4. Set up ngrok;
5. Run the server;
6. Enjoy!

## 1. **CLONE THE REPOSITORY**
```bash
git clone https://github.com/pennyw1ze/gmail_webhook_handler
```