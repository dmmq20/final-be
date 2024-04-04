from app.utils import hash_password

userData = [("Edgar Burke", hash_password("secret123"), "https://miro.medium.com/v2/resize:fit:1020/1*jZ9v-2QShwnfCwHlEZCmDw.png"),
            ("Eloy Erikson", hash_password("password123"),
             "https://assets-global.website-files.com/636b968ac38dd1495ec4edcd/63ce5755b45e867c12c9b3cb_socials_profile.webp"),
            ("Claire Hayes", hash_password("mypassword"),
             "https://miro.medium.com/v2/resize:fit:530/1*Zq3nm98-v7zBWnNspGGXhA.jpeg"),
            ("Martha Robertson", hash_password("strongpassword"),
             "https://pfpmaker.com/images/ai/examples/first/results/result-pic-1.png"),
            ("Todd Hoover", hash_password("verysecure"), "https://preview.redd.it/transform-your-selfie-into-a-stunning-ai-avatar-with-stable-v0-2z411m9dob6a1.png?width=1024&format=png&auto=webp&s=8e97db53d8c34044ce841f0110cf996fbd28f006")]
