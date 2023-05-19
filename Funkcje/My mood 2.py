def my_mood(answear):
    print("My mood: ")
    return answear * 2

resp = input("How are you?")
twiced = my_mood(resp)
print("My mood is like", twiced)