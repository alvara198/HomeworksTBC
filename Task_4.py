Speed = int(input("შეიყვანეთ ავტომობილის სიჩქარე: "))

if Speed > 120:
    print("თქვენი ავტომობილის სიჩქარის კატეგორია არის: VERY FAST")
elif Speed > 60:
    print("თქვენი ავტომობილის სიჩქარის კატეგორია არის: FAST")
elif Speed > 30:
    print("თქვენი ავტომობილის სიჩქარის კატეგორია არის: MODERATE")
else:
    print("თქვენი ავტომობილის სიჩქარის კატეგორია არის: SLOW")
