## Get App Password (for gmail)

the steps below will walk you through generating an app password token to be used in [main.py](https://github.com/coleman-zachery/send_email/blob/main/main.py) in order to enable logging in to your gmail account and send email messages via the python script.

---

1.   login to your gmail account, click gear icon, and then click "See all settings"

![image](https://github.com/coleman-zachery/send_email/assets/42438576/5f9b7ffa-04fa-4878-a918-3cb3cbb65bb2)

---

2.   click "Accounts and Import" tab and then click "Other Google Account Settings"

![image](https://github.com/coleman-zachery/send_email/assets/42438576/fefd767c-34a0-4e74-be84-a554dead3b90)

---

3a. click "Security", scroll down, and ensure "2-Step Verification" is on. click on it if it is off and follow the rest of step 3

![image](https://github.com/coleman-zachery/send_email/assets/42438576/a8343060-79a5-40f5-be21-82b188470112)

---

3b. click "Get Started"

![image](https://github.com/coleman-zachery/send_email/assets/42438576/d958317d-1b8a-425a-af0b-6d023daa4dcb)

---

3c. click "Continue"

![image](https://github.com/coleman-zachery/send_email/assets/42438576/90e2b9bd-b04a-4c1f-bf59-7bf8a2b2d9e1)

---

3d. enter your phone number and click "Send"

![image](https://github.com/coleman-zachery/send_email/assets/42438576/c74767cc-2318-423c-96df-6f0b9aad7a77)

---

3e. enter code from text message / phone call and click "Next"

![image](https://github.com/coleman-zachery/send_email/assets/42438576/ef71ef02-f1d6-4666-927e-76230175e113)

---

3f. click "Turn On" (2-Step Verification should now be "On")

![image](https://github.com/coleman-zachery/send_email/assets/42438576/4a269833-c86b-4236-92d2-9ad5421549c4)

![image](https://github.com/coleman-zachery/send_email/assets/42438576/dfe59fd9-cc6e-43bc-a684-b0bc4c7c7bd2)

---

4.   go back to Google Account and search for "App passwords"

![image](https://github.com/coleman-zachery/send_email/assets/42438576/1027d01a-6227-415f-ad27-5116fabb86ce)

---

5.   create an app password by giving it a name like "python_email", and click "create"

![image](https://github.com/coleman-zachery/send_email/assets/42438576/78b84982-8a3f-445f-aa1b-610b8da5fb9b)

---

6.   save the generated app password as a string into your .py script:

![image](https://github.com/coleman-zachery/send_email/assets/42438576/7e628c85-1de0-4719-ae19-ff66a146bbc8)

``` python
my_password = 'aaaa aaaa aaaa aaaa'
```

---

7.   click "Done"

![image](https://github.com/coleman-zachery/send_email/assets/42438576/eb0fb932-b401-4dae-a4ae-afae43e54fd4)

---

8.   you can also delete it when no longer needed or to refresh the token with new credentials, or make multiple app passwords

![image](https://github.com/coleman-zachery/send_email/assets/42438576/6f20add4-8014-49ed-bfc8-2d9322f7d2a4)
