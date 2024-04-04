from app.utils import hash_password

userData = [("Edgar Burke", hash_password("secret123"), "https://miro.medium.com/v2/resize:fit:1020/1*jZ9v-2QShwnfCwHlEZCmDw.png"),
            ("Eloy Erikson", hash_password("password123"),
             "https://assets-global.website-files.com/636b968ac38dd1495ec4edcd/63ce5755b45e867c12c9b3cb_socials_profile.webp"),
            ("Claire Hayes", hash_password("mypassword"),
             "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/79265ebb-a30b-487c-8762-c584c0f4b5ac/dfy3ub4-4a01510b-8536-4947-84f0-0a9e73e4ec76.jpg/v1/fill/w_1280,h_1670,q_75,strp/hi_i_am_aida__your_personal_ai_avatar_by_ishi99_dfy3ub4-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTY3MCIsInBhdGgiOiJcL2ZcLzc5MjY1ZWJiLWEzMGItNDg3Yy04NzYyLWM1ODRjMGY0YjVhY1wvZGZ5M3ViNC00YTAxNTEwYi04NTM2LTQ5NDctODRmMC0wYTllNzNlNGVjNzYuanBnIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.IisRKNqsQxylN6mr9xMWttZ_9a4wjhKD36H5nz8Q4QE"),
            ("Martha Robertson", hash_password("strongpassword"),
             "https://pfpmaker.com/images/ai/examples/first/results/result-pic-1.png"),
            ("Todd Hoover", hash_password("verysecure"), "https://preview.redd.it/transform-your-selfie-into-a-stunning-ai-avatar-with-stable-v0-2z411m9dob6a1.png?width=1024&format=png&auto=webp&s=8e97db53d8c34044ce841f0110cf996fbd28f006")]
