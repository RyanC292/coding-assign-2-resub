# ---------------- EVENTS ---------------- #

events = {
    "Football": "Team",
    "Basketball": "Team",
    "Tennis": "Individual",
    "Swimming": "Individual"
}

# Define teams and players
teams = {
    "Team A": ["A1", "A2", "A3", "A4", "A5"],
    "Team B": ["B1", "B2", "B3", "B4", "B5"],
    "Team C": ["C1", "C2", "C3", "C4", "C5"],
    "Team D": ["D1", "D2", "D3", "D4", "D5"]
}


# ---------------- INDIVIDUAL SETUP ---------------- #

# 20 individual competitor slots
individuals = {f"Player {i}": 0 for i in range(1, 21)}

# Store registrations (multiple events allowed)
registrations = {
    "Football": set(),
    "Basketball": set(),
    "Tennis": set(),
    "Swimming": set()
}

# Event-specific scores
event_scores = {
    event: {} for event in events
}


# ---------------- FUNCTIONS ---------------- #

def show_events():
    print("\n--- Events ---")
    for name, category in events.items():
        print(f"- {name} ({category})")


# ---------- REGISTRATION ---------- #

def register_competitor():
    show_events()
    event = input("\nEnter event name: ").strip()

    if event not in events:
        print("❌ Invalid event.")
        return

    category = events[event]

    if category == "Team":
        print("\nAvailable Teams:")
        for team in teams:
            print("-", team)

        name = input("Enter team name: ").strip()

        if name not in teams:
            print("❌ Invalid team.")
            return

    else:
        print("\nAvailable Individuals:")
        for person in individuals:
            print("-", person)

        name = input("Enter individual name: ").strip()

        if name not in individuals:
            print("❌ Invalid individual.")
            return

    # Allow multiple events (no restriction)
    registrations[event].add(name)

    # Initialize score for event if not already
    if name not in event_scores[event]:
        event_scores[event][name] = 0

    print(f"✅ {name} successfully registered for {event}!")


# ---------- RECORD RESULT ---------- #

def record_result():
    show_events()
    event = input("\nEnter event name: ").strip()

    if event not in events:
        print("❌ Invalid event.")
        return

    if not registrations[event]:
        print("❌ No competitors registered for this event.")
        return

    print("\nRegistered Competitors:")
    for competitor in registrations[event]:
        print("-", competitor)

    winner = input("Enter winner name: ").strip()

    if winner not in registrations[event]:
        print("❌ Competitor not registered in this event.")
        return

    # Award points (5 per win)
    event_scores[event][winner] += 5

    # Add to overall totals
    if events[event] == "Team":
        teams[winner] += 5
    else:
        individuals[winner] += 5

    print(f"🏆 {winner} earns 5 points in {event}!")


# ---------- EVENT RANKINGS ---------- #

def show_event_rankings():
    show_events()
    event = input("\nEnter event name: ").strip()

    if event not in event_scores:
        print("❌ Invalid event.")
        return

    print(f"\n🏅 Rankings for {event}")

    rankings = sorted(event_scores[event].items(),
                      key=lambda x: x[1],
                      reverse=True)

    if not rankings:
        print("No results yet.")
        return

    for pos, (name, points) in enumerate(rankings, start=1):
        print(f"{pos}. {name} - {points} pts")


# ---------- OVERALL LEADERBOARD ---------- #

def show_overall_leaderboard():
    print("\n🏆 --- OVERALL LEADERBOARD ---")

    combined = {}

    # Add team totals
    for team, pts in teams.items():
        combined[team] = pts

    # Add individual totals
    for person, pts in individuals.items():
        combined[person] = pts

    rankings = sorted(combined.items(),
                      key=lambda x: x[1],
                      reverse=True)

    for pos, (name, points) in enumerate(rankings, start=1):
        print(f"{pos}. {name} - {points} pts")


# ---------------- MAIN MENU ---------------- #

while True:
    print("\n=== TOURNAMENT SYSTEM ===")
    print("1. Register for event (multiple allowed)")
    print("2. Record event result")
    print("3. View event rankings")
    print("4. View overall leaderboard")
    print("5. Exit")

    choice = input("Choose option (1-5): ").strip()

    if choice == "1":
        register_competitor()
    elif choice == "2":
        record_result()
    elif choice == "3":
        show_event_rankings()
    elif choice == "4":
        show_overall_leaderboard()
    elif choice == "5":
        print("Tournament ended.")
        break
    else:
        print("❌ Invalid choice.")






