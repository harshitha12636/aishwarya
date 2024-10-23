class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __str__(self):
        return f"{self.name}: {self.votes} votes"

class VotingSystem:
    def __init__(self):
        self.candidates = []
        self.voters = set()

    def add_candidate(self, name):
        candidate = Candidate(name)
        self.candidates.append(candidate)

    def cast_vote(self, voter_id, candidate_name):
        if voter_id in self.voters:
            print("You have already voted.")
            return False

        for candidate in self.candidates:
            if candidate.name == candidate_name:
                candidate.votes += 1
                self.voters.add(voter_id)
                print(f"Vote casted for {candidate_name}.")
                return True

        print("Candidate not found.")
        return False

    def view_results(self):
        print("\nElection Results:")
        for candidate in self.candidates:
            print(candidate)

def main():
    voting_system = VotingSystem()
    
    while True:
        print("\nOnline Voting System")
        print("1. Add Candidate")
        print("2. Cast Vote")
        print("3. View Results")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            candidate_name = input("Enter candidate name: ")
            voting_system.add_candidate(candidate_name)
            print(f"Candidate '{candidate_name}' added successfully.")

        elif choice == '2':
            voter_id = input("Enter your voter ID: ")
            candidate_name = input("Enter candidate name to vote for: ")
            voting_system.cast_vote(voter_id, candidate_name)

        elif choice == '3':
            voting_system.view_results()

        elif choice == '4':
            print("Exiting system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
