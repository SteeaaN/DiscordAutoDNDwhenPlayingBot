# DiscordAutoDNDwhenPlaying

## Setting Up

<details>
  <summary>Step 1 - Download the bot source files</summary>

  Go to the [releases section](https://github.com/SteeaaN/DiscordAutoDNDwhenPlayingBot/releases), choose the latest release, and download **Source code (zip)**.
</details>

<details>
  <summary>Step 2 - Enable developer mode</summary>

  Go to Discord settings -> Advanced -> Enable developer mode.
</details>

<details>
  <summary>Step 3 - Create a Discord server</summary>

  A basic server with one text channel for logs is enough.  
  **P.S.** If you want the Active Developer Badge, you can create a community server and use the `/ping` command once every 30 days.  
  More details [here](https://support-dev.discord.com/hc/en-us/articles/10113997751447-Active-Developer-Badge).
</details>

<details>
  <summary>Step 4 - Setting up necessary data</summary>

  Open the `const.py` file.

  - Go back to Discord -> Right-click on the icon of the created server -> Copy ID  
  - Paste the copied ID after `guild_id = ` in the open file  
  - Right-click on the log text channel in Discord -> Copy ID  
  - Paste the copied ID after `log_channel_id = `  
  - Right-click on yourself in the member list -> Copy ID  
  - Paste the copied ID after `user_id = `

  **Optional:** Increase the `delay` to reduce potential load.

  Then, in Discord, press **Ctrl + Shift + I** (for the app) or **F12** (for the browser). In the top of the opened panel, find the **Network** tab (may be hidden under two arrows).  
  Change your status to **DND**. Find a line with `1` in the **Name** column and click on it.  
  In the **Headers** section, find the `authorization:` header and copy its value.  

  Open the downloaded `auth_token.txt` file, delete its content, paste the copied value, and save the file.  

  In the **Payload** section of the same request, copy the value of `settings` without quotes.
  Open the downloaded `dnd_status.txt` file, delete its content, paste the copied value, and save the file.

  Change your status to **Online** and similarly change the `online_status.txt` file.

  Then, update the `games` list in the same file with your desired games.
</details>

<details>
  <summary>Step 5 - Create a bot</summary>

  Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application.  
  Go to the **Installation** section and choose **None** for the install link.  
  In the **Bot** section, disable **Public Bot**, enable **Presence Intent**, **Server Members Intent**, and **Message Content Intent**.  
  Reset the bot token by clicking **Reset Token**, copy the token, and paste it into `const.py` after `bot_token = ` between single quotes. Save and close the file.
</details>

<details>
  <summary>Step 6 - Invite the bot to your server</summary>

  Go to the **OAuth2** section of the Developer Portal, and under **Scopes**, select `bot`. Under **Bot Permissions**, select `Administrator`.  
  Copy the generated link below and invite the bot to the created server.
</details>

<details>
  <summary>Step 7 - Install Python</summary>

  The minimum Python version for the bot is **3.8**.  
  [Download Python here](https://www.python.org/downloads/).  
  Ensure that you add Python to your PATH.
</details>

<details>
  <summary>Step 8 - Install necessary libraries</summary>

  Open a terminal and navigate to the directory with the bot files.  
  Install the required libraries using the following command:

  ```bash
  pip install -r requirements.txt
  ```
</details>
<details> 
  <summary>Step 9 - Start the bot</summary>
  
  Run the bot using the 'bot.py' file.

</details>

## Commands

- Every time your token changes, use the command:  
  ```bash
  /token your_new_token_without_quote
  ```
- Every time you change the status (text and emoji), use the following commands:
  ```bash
  /online_status your_new_online_status_without_quote
  ```
  
  ```bash
  /dnd_status your_new_dnd_status_without_quote
  ```
  
**P.S.** Check Step 4










  
