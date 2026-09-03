print("hello world")
bjp_votes = 0
congress_votes = 0

voters = int(input("Enter number of voters: "))

for voter in range(voters):
    print("\n1. BJP")
    print("2. Congress")

    choice = input("Enter your vote: ")

    if choice == "1":
        bjp_votes += 1
    elif choice == "2":
        congress_votes += 1
    else:
        print("Invalid vote")

print("\nElection Result")
print("BJP:", bjp_votes, "votes")
print("Congress:", congress_votes, "votes")

if bjp_votes > congress_votes:
    print("BJP wins the election")
elif congress_votes > bjp_votes:
    print("Congress wins the election")
else:
    print("The election is tied")