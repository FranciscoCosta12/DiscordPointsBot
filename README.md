# 🤖 Discord Points Bot

A simple Discord bot to manage user points on a server. Users can give or remove points from each other with a reason.

## 📚 Features

- Check a user's points
- Give or remove points with justification
- No upper/lower point limit (points can go negative)
- Prevent users from editing their own score

## 🚀 Deploy on Railway

### 1. Clone this repository

```bash
git clone https://github.com/your-profile/discord-points-bot.git
cd discord-points-bot
```

## 📜 Available Commands

| Command | Description |
|--------|-------------|
| `!points_of @user` | Shows the mentioned user's points. |
| `!give_points @user amount reason` | Adds amount point to the user with a reason (you can't give points to yourself). |
| `!remove_points @user amount reason` | Removes amount point from the user with a reason (you can't remove points from yourself). |


