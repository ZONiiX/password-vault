import random

randomizer = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

passLength = 8

generatePassword = ''.join(random.sample(randomizer, passLength))

print (generatePassword)