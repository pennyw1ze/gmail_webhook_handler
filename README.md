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
3. Set up ngrok;
4. Set up the webhook on your gmail account;
5. Customize the webhook handler and run the server;
6. Enjoy!

## 1. **CLONE THE REPOSITORY**
```bash
git clone https://github.com/pennyw1ze/gmail_webhook_handler
```

## 2. **INSTALL THE REQUIREMENTS**
- First, you need to install python3 and pip3 on your machine.
```bash
sudo apt install python3 python3-pip
```
- Then, you need to install and create a virtual environment to install the pip packages:
```bash
pip install virtualenv
sudo apt install python3.10-venv
python3 -m venv myenv
source myenv/bin/activate
```
> [!NOTE]
> - If you are using windows, you can create a virtual environment with the following command:
> ```bash
> python -m venv myenv
> myenv\Scripts\activate
> ```

- Finally, you can install the requirements:
```bash
cd gmail_webhook_handler
pip install -r requirements.txt
```

- Once you are done, you can deactivate the virtual environment with the following command:
```bash
deactivate
```

## 3. **SET UP NGROK**
- Log in or create an account on [ngrok](https://ngrok.com/);
- Follow the instructions to set up ngrok on your machine. Here I report instructions for linux:
```bash
curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
	| sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
	&& echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
	| sudo tee /etc/apt/sources.list.d/ngrok.list \
	&& sudo apt update \
	&& sudo apt install ngrok

ngrok config add-authtoken <your_auth_token>
```
- Once you are done, go in the 'Setup & Installation' section and look for your static domain;
- The domain will be in the form:
> ngrok http --url=<your_address_here> 80
- Pic the --url=<your_address_here> and copy paste it in the data/ngrok_url_sample.txt file and rename it to ngrok_url.txt;
```bash
mv data/ngrok_url_sample.txt data/ngrok_url.txt
```
- Run the command provided by ngrok to start the tunnel (just for testing, the bot will run the server holding the ngrok url):
```bash
ngrok http --url=<domain_name> 80
```

## 4. **SET UP THE WEBHOOK ON YOUR GMAIL ACCOUNT**
- To set up gmail webhook you can find a usefull guide [here](https://hevodata.com/learn/gmail-webhook/);
- Download the secret.json file and put it in the data folder;
- Run the following command to get the authorization token (you will be asked to access with your google account and grant permission to read email):
```bash
cd scripts
python3 get_access_token.py
```
- The token will be saved in the data folder as token.pickle;
- You will also need to run the set_watch_function to set up the webhook on your gmail account:
```bash
python3 set_watch_function.py
```
- This function must be ran every day to keep the webhook alive. You can set up a cron job to do this automatically:
```bash
crontab -e
```
- Add the following line to the crontab file (substitute /path/to/gmail_webhook_handler with the path to the cloned repository):
```bash
0 0 * * * /usr/bin/python3 /path/to/gmail_webhook_handler/scripts/set_watch_function.py
```

## 5. **CUSTOMIZE THE WEBHOOK HANDLER AND RUN THE SERVER**
- Customize the gmail_functions.py file to implement your own webhook handler;
- You can use the following functions to interact with the email. The email is a dictionary with the following keys:
```python
{
	"subject": "The subject of the email",
	"from": "The sender of the email",
	"to": "The receiver of the email",
	"date": "The date of the email",
	"body": "The body of the email",
	"attachments": "The attachments of the email"
}
```
- Send an email to your gmail account to test the webhook handler and start playing with it;

- Run the server with the following command:
```bash
python3 main.py
```

## 6. **ENJOY!**
Have fun 😊

