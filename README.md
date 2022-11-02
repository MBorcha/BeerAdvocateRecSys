# BeerAdvocateRecSys

## Short description
Developing a recommender system which offers a sort of beer based on a client's preferences.

## Data
"BeerAdvocate" is a web-site which contains comments and rates related to different sorts of beer. The data span a period of more than 10 years, including all ~1.5 million reviews up to November 2011. Each review includes ratings in terms of five "aspects": appearance, aroma, palate, taste, and overall impression. Reviews include product and user information, followed by each of these five ratings, and a plaintext review.

Text of reviews

## Quality evaluation
A developed model is compared with a provided baseline algorithm.
The idea of the baseline is following: if a clients try (and review) one sort of beer after another one, they believe that the sort of beer should satisfy their expectations (be tasty, etc.)
So recommending a sort of beer which is the following for the most of clients, is a way to follow their preferences as well as rather simple method which does not require anything except the chains of reviews provided by other clients.
At the same time it's a universal baseline which can be applied to any existing client, but not to a new client.
For a new client there can be chosen a random sort.

## Design of the application
1. Sign-in or sign-up
2. Ask questions about preferences (for a new client) or/and "Describe what you want right now"
3. Making recommendations based on the previously added information as well as info which was provided on the previous step
4. Ask for a feedback (review) after some time

## ToDo list
* [x] Define functional requirements to the ML system (what the system does)
* [] Define non-functional requirements to the ML system (reliable, scalable, maintainable, adaptable)
* [] How to measure success (metrics)
* [] Decision about an interface
* [] Decision about algorithms
* [] Decision about hardware and software based on the initial requirements
* [x] Upload the initial dataset (Source: https://www.kaggle.com/datasets/rdoume/beerreviews)
* [x] What data is required additionally
* [] Data exploration
* [] Revise RecSys theory and approaches
* [] What about a monitoring process?
* [x] Naive solution without ML (as a baseline), or existing solution