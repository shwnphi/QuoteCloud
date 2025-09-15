import boto3
import priv



#Quotes

Quotes = [
    {
        "id": "1",
        "text": "It is never too late to be what you might have been",
        "author": "George Elliot",
    },

    {
        "id": "2",
        "text": "The only way to do great work is to love what you do",
        "author": "Steve Jobs ",
    },

    {
        "id": "3",
        "text": "Believe you can and you're halfway there",
        "author": "Theodore Roosevelt",
    },

    {
        "id": "4",
        "text": "It always seems impossible until it's done",
        "author": "Nelson Mandela",
    },

    {
        "id": "5",
        "text": "Be the change that you wish to see in the world",
        "author": "Mahatma Ghandi",
    },

     {
        "id": "6",
        "text": "Success is not final, failure is not fatal: it is the courage to continue that counts",
        "author": "Winston Churchill",
    },

     {
        "id": "7",
        "text": "Don't watch the clock; do what it does. Keep going",
        "author": "Sam Levenson",
    },

     {
        "id": "8",
        "text": "The only person you are destined to become is the person you decide to be.",
        "author": "Ralph Waldo Emerson",
    },

     {
        "id": "9",
        "text": "Either you run the day or the day runs you.",
        "author": "Jim Rohn",
    },

    {
        "id": "10",
        "text": "I like the dreams of the future better than the history of the past",
        "author": "Thomas Jefferson",
    },

     {
        "id": "11",
        "text": "I’m a great believer in luck, and I find the harder I work, the more I have of it",
        "author": "Thomas Jefferson",
    },

    {
        "id": "12",
        "text": "Women challenge the status quo because we are never it",
        "author": "Cindy Gallop",
    },

    {
        "id": "13",
        "text": "If they dont give you a seat at the table, bring a folding chair",
        "author": "Shirley Chisholm",
    },

    {
        "id": "14",
        "text": "The mose difficult thing is the decision to act; the rest merely tenacity",
        "author": "Amelia Earhart",
    },

    {
        "id": "15",
        "text": "Success is stumbling from failure to failure with no loss of enthusiasm",
        "author": "Winston Churchill",
    },

    {
        "id": "16",
        "text": "Get a good idea and stay with it. Dog it, and work at it until it's done right",
        "author": "Walt Disney",
    },

    {
        "id": "17",
        "text": "Optimism is the faitl that leads to achievement. Nothing can be done without hope and confidence",
        "author": "Helen Keller",
    },

    {
        "id": "18",
        "text": "People say nothing is impossible, but I do nothing every day",
        "author": "Winnie the Pooh",
    },

    {
        "id": "19",
        "text": "Talen wins games, but teamwork and intelligence win championships",
        "author": "Micheal Jordan",
    },

    {
        "id": "20",
        "text": "Individual commitment to a group effort—that is what makes a team work, a company work, a society work, a civilization work.",
        "author": "Vince Lombardi",
    },

    {
        "id": "21",
        "text": "Opportunities don’t happen, you create them.",
        "author": "Chris Grosser",
    },

    {
        "id": "22",
        "text": "If you’re not positive energy, you’re negative energy",
        "author": "Mark Cuban",
    },

    {
        "id": "23",
        "text": "If you can dream it, you can do it",
        "author": "Walt Disney",
    },

    {
        "id": "24",
        "text": "Love your family, work super hard, live your passion",
        "author": "Gary Vaynerchuk",
    },

    {
        "id": "25",
        "text": "Don’t let someone else’s opinion of you become your reality",
        "author": "Les Brown",
    },

    {
        "id": "26",
        "text": "Do the best you can. No one can do more that that",
        "author": "John Wooden",
    },

    {
        "id": "27",
        "text": "Inspiration does exist, but it must find you working",
        "author": "Pablo Picasso",
    },

    {
        "id": "28",
        "text": "I have stood on a mountain of no's for one yes",
        "author": "Barara Elaine Smith",
    },

    {
        "id": "29",
        "text": "Don’t bunt. Aim out of the ballpark. Aim for the company of immortals",
        "author": "David Ogilvy",
    },

    {
        "id": "30",
        "text": "Dont look at ypur feet to see if you are doing it right. Just dance",
        "author": "Anne Lammot",
    },

]


# Sends Quotes to DynamoDB in batches
with priv.table.batch_writer() as batch:
    for quote in Quotes:
        batch.put_item(Item=quote)





