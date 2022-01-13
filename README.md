# News
DEPLOYMENT LINK: https://narminnews.herokuapp.com/api/v1.0/posts/ ( original https://narminnews.herokuapp.com/ )

POSTMAN LINK: https://www.postman.com/speeding-spaceship-957949/workspace/news

If you want to run this project locally follow below steps.
1. First of all, you have to run python3 -m venv venv - to install virtualenv in your pyoject directory. 
2. Then download everything in requirements.txt by running command pip3 install -r requirements.txt or  pip install -r requirements.txt (Python 2).
3. We have two docker-compose files one is to run local and the other for deployment. So go to _development folder and run docker-compose.yml. Then cd .. and ./manage.py runserver to run our project. 
4. We have basic CRUD API, but to Put, Delete and Patch methods you have to authenticate. For this we have register/ and login/ endpoints. First register(shown in image) {"username": " ", "password": " ", "email": " " } like this in Json format. Fill in blank spaces. Then login by Username and Password, I am sending back only token and it contains username, email and user id.

5. <img width="1056" alt="Screen Shot 2022-01-13 at 21 04 55" src="https://user-images.githubusercontent.com/79960958/149388415-ba8db745-132e-4288-9f0e-aaab29613e19.png"> <img width="1119" alt="Screen Shot 2022-01-13 at 21 05 04" src="https://user-images.githubusercontent.com/79960958/149388506-07753d0f-d59c-4c9c-b5bf-ce64bc937f38.png">
6. Copy Token and keep it, you will need it. Token is Bearer token. 
7.Create a post <img width="1072" alt="Screen Shot 2022-01-13 at 21 07 13" src="https://user-images.githubusercontent.com/79960958/149388723-5cdf10f0-ea28-4751-8d49-b93ce25f2cd0.png">
8. Now have a look at all posts that we have in our database <img width="1121" alt="Screen Shot 2022-01-13 at 21 07 23" src="https://user-images.githubusercontent.com/79960958/149388825-070d6941-72cf-4257-b86b-9a279d3135bb.png">
9. If we try to make changes to certain post it will ask us post's author's token. Only author who created that post is able to make changes to that post and same logic applies to delete method.(the same thing applies to comments) At the first image I copied other person's token so it returned message that I am not allowed to do so. <img width="1125" alt="Screen Shot 2022-01-13 at 21 11 58" src="https://user-images.githubusercontent.com/79960958/149389021-55b42123-2f06-47a8-887d-a69ec0885830.png"> 
10. But here I can because token user is same with post author . <img width="1148" alt="Screen Shot 2022-01-13 at 21 12 34" src="https://user-images.githubusercontent.com/79960958/149389588-b9784a52-b3cf-4c72-a177-4f42bb5a89c8.png"> 
11. Next step let's Upvote a post. For this you also have to be logged in as only they can upvote. <img width="1102" alt="Screen Shot 2022-01-13 at 21 08 46" src="https://user-images.githubusercontent.com/79960958/149390679-de5de2b3-eb5f-4618-b3ed-2d4eccb9b7fd.png">
You can upvote only once.
<img width="1130" alt="Screen Shot 2022-01-13 at 21 08 54" src="https://user-images.githubusercontent.com/79960958/149390713-727750c8-1eb0-40ed-9286-cea96fa5e08c.png">

12. Now we have to take same steps to comments. In put method you don't need to send author it will take it automatically from token and set it. 
<img width="1119" alt="Screen Shot 2022-01-13 at 22 10 36" src="https://user-images.githubusercontent.com/79960958/149391631-fccb8164-f691-4229-a809-359382fbbdf5.png">


13. We can look at comments under specific post
<img width="1134" alt="Screen Shot 2022-01-13 at 22 12 53" src="https://user-images.githubusercontent.com/79960958/149391662-03bcea41-9cf9-43e7-909e-14804e96706f.png">






