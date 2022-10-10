# Discord-movie-bot
This is a Discord movie chatbot that is focused around facilitating human-like responses for a fun and convenient user experience. The primary goals of the chatbot is to allow users to create, save and access movie watchlists, as well as to fetch YouTube trailers for any desired movie. Secondary features include basic, human-like responses to conversations initiated by the user, and a 'quote' function that prompts the chatbot to return a random quote from a popular movie.

As for the technologies used to implement the chatbot, Python was the preferred language considering it's ideal for scripting, simplicity and excellent portablity. The Discord API is also highly compatible with Python, which was used to instantiate a bot that connects and interacts with Discord servers. Additionally, a relational database was implemented for storing user information like watchlists, and the choice to utilise SQL as opposed to noSQL was primarily due to the data being small, which didn't warrant a particularly scalable database, hence SQL was chosen for high consistency and speed of access. The YouTube API was utilised in tandem with the Discord API to interact with Discord servers for the purpose of taking user input that is used to look for trailers with matching names.
