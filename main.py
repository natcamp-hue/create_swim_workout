from drafter import *
from dataclasses import dataclass

set_website_title("SwimSet")
set_site_information(
    author="Natalie Campbell",
    description="Create a swim set for a workout.",
    sources="Thanks to the Drafter docs and ChatGPT.",
    planning="CS1_Doc_1.pdf",
    links=["file:///C:/Users/ngc19/Downloads/CS1%20Final%20Project%201_%20Design.pdf"]
)
hide_debug_information()
set_website_framed(False)

# --------------------------------------------------
# DATACLASSES
# --------------------------------------------------

@dataclass
class SwimSet:
    """
    Represents one complete swimming workout.

    Each workout contains a warmup, main set, and
    cooldown. The workout also stores its difficulty,
    training focus, and total distance.
    """
    name: str
    skill_level: str
    workout_focus: str
    warmup: list[str]
    main_set: list[str]
    cooldown: list[str]
    total_distance: int


@dataclass
class State:
    """
    Stores all information that the website needs.

    The State dataclass remembers user preferences,
    the currently generated workout, saved favorites,
    and the collection of available workouts.
    """
    skill_level: str
    workout_focus: str
    distance_goal: int
    current_workout: SwimSet | None
    favorite_workouts: list[SwimSet]
    workout_library: list[SwimSet]


# --------------------------------------------------
# WORKOUT LIBRARY
# --------------------------------------------------

def create_workout_library() -> list[SwimSet]:
    """
    Creates the collection of available swim workouts.

    Each SwimSet is stored as an instance in a list.
    The generator uses this list to find an appropriate
    workout based on the user's preferences.
    """

    library = [

        # BEGINNER WORKOUTS

        SwimSet(
            "Beginner Endurance",
            "Beginner",
            "Endurance",
            ["200 easy freestyle", "4 x 50 kick"],
            ["4 x 100 freestyle at an easy pace",
             "4 x 50 freestyle with 20 seconds rest"],
            ["100 easy choice"],
            1300
        ),

        SwimSet(
            "Beginner Sprint",
            "Beginner",
            "Sprint",
            ["200 easy freestyle", "4 x 25 kick"],
            ["4 x 25 fast freestyle",
             "4 x 50 easy freestyle",
             "4 x 25 fast freestyle"],
            ["100 easy choice"],
            900
        ),

        SwimSet(
            "Beginner Pace Training",
            "Beginner",
            "Pace Training",
            ["200 easy freestyle", "4 x 50 freestyle"],
            ["4 x 50 freestyle at a consistent pace",
             "4 x 25 freestyle focusing on even pacing"],
            ["100 easy choice"],
            700
        ),

        SwimSet(
            "Beginner Technique",
            "Beginner",
            "Technique",
            ["200 easy freestyle"],
            ["4 x 50 freestyle focusing on body position",
             "4 x 50 kick",
             "4 x 25 catch-up drill"],
            ["100 easy choice"],
            900
        ),

        SwimSet(
            "Beginner Recovery",
            "Beginner",
            "Recovery",
            ["200 easy freestyle"],
            ["4 x 50 easy freestyle",
             "4 x 50 backstroke",
             "4 x 25 easy choice"],
            ["100 easy choice"],
            800
        ),

        # INTERMEDIATE WORKOUTS

        SwimSet(
            "Intermediate Endurance",
            "Intermediate",
            "Endurance",
            ["300 freestyle", "4 x 50 kick"],
            ["5 x 200 freestyle at an aerobic pace",
             "4 x 100 pull"],
            ["200 easy choice"],
            1900
        ),

        SwimSet(
            "Intermediate Sprint",
            "Intermediate",
            "Sprint",
            ["300 freestyle", "4 x 50 kick"],
            ["8 x 50 sprint",
             "4 x 100 easy freestyle",
             "8 x 25 sprint"],
            ["200 easy choice"],
            1700
        ),

        SwimSet(
            "Intermediate Pace Training",
            "Intermediate",
            "Pace Training",
            ["300 freestyle", "4 x 50 build"],
            ["8 x 100 freestyle at goal pace",
             "4 x 50 maintaining consistent splits"],
            ["200 easy choice"],
            1700
        ),

        SwimSet(
            "Intermediate Technique",
            "Intermediate",
            "Technique",
            ["300 freestyle"],
            ["4 x 100 drill/swim by 25",
             "4 x 100 pull focusing on technique",
             "4 x 50 kick"],
            ["200 easy choice"],
            1700
        ),

        SwimSet(
            "Intermediate Recovery",
            "Intermediate",
            "Recovery",
            ["300 easy freestyle"],
            ["4 x 100 easy freestyle",
             "4 x 50 backstroke",
             "4 x 50 easy choice"],
            ["200 easy choice"],
            1300
        ),

        # ADVANCED WORKOUTS

        SwimSet(
            "Advanced Endurance",
            "Advanced",
            "Endurance",
            ["400 freestyle", "4 x 100 kick"],
            ["6 x 200 freestyle",
             "4 x 100 pull",
             "4 x 100 freestyle"],
            ["300 easy choice"],
            2800
        ),

        SwimSet(
            "Advanced Sprint",
            "Advanced",
            "Sprint",
            ["400 freestyle", "4 x 50 build"],
            ["12 x 50 sprint",
             "8 x 25 all-out sprint",
             "4 x 100 easy recovery"],
            ["300 easy choice"],
            2000
        ),

        SwimSet(
            "Advanced Pace Training",
            "Advanced",
            "Pace Training",
            ["400 freestyle", "4 x 50 build"],
            ["10 x 100 at goal race pace",
             "4 x 200 holding consistent splits"],
            ["300 easy choice"],
            2600
        ),

        SwimSet(
            "Advanced Technique",
            "Advanced",
            "Technique",
            ["400 freestyle"],
            ["8 x 100 drill/swim",
             "4 x 100 pull",
             "8 x 50 kick"],
            ["300 easy choice"],
            2500
        ),

        SwimSet(
            "Advanced Recovery",
            "Advanced",
            "Recovery",
            ["400 easy freestyle"],
            ["4 x 200 easy freestyle",
             "4 x 100 backstroke",
             "4 x 50 easy choice"],
            ["300 easy choice"],
            2100
        ),

        # ADDITIONAL WORKOUT OPTIONS

        SwimSet(
            "Distance Challenge",
            "Advanced",
            "Endurance",
            ["500 freestyle", "4 x 100 kick"],
            ["3 x 500 freestyle",
             "4 x 100 pull"],
            ["300 easy choice"],
            2900
        ),

        SwimSet(
            "Short Sprint Challenge",
            "Intermediate",
            "Sprint",
            ["300 freestyle", "4 x 50 build"],
            ["16 x 25 sprint",
             "8 x 50 easy freestyle"],
            ["200 easy choice"],
            1500
        ),

        SwimSet(
            "Aerobic Builder",
            "Intermediate",
            "Endurance",
            ["300 freestyle", "4 x 50 kick"],
            ["3 x 300 freestyle",
             "4 x 100 pull"],
            ["200 easy choice"],
            2100
        ),

        SwimSet(
            "Race Preparation",
            "Advanced",
            "Pace Training",
            ["400 freestyle", "4 x 50 build"],
            ["4 x 100 at race pace",
             "4 x 50 faster than race pace",
             "4 x 200 aerobic"],
            ["300 easy choice"],
            2300
        ),

        SwimSet(
            "Easy Technique Day",
            "Beginner",
            "Technique",
            ["200 easy freestyle"],
            ["4 x 50 kick",
             "4 x 50 catch-up drill",
             "4 x 50 easy freestyle"],
            ["100 easy choice"],
            900
        )
    ]

    return library


# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------

def find_workout(state: State) -> SwimSet | None:
    """
    Finds the workout that best matches the user's
    selected skill level, training focus, and distance.

    The function searches through the workout library
    and selects the closest matching workout.
    """

    matching_workouts = []

    # Find workouts matching the user's preferences.
    for workout in state.workout_library:

        if workout.skill_level == state.skill_level:
            if workout.workout_focus == state.workout_focus:
                matching_workouts.append(workout)

    # If there are no matching workouts, return None.
    if len(matching_workouts) == 0:
        return None

    # Choose the workout with the closest distance.
    best_workout = matching_workouts[0]
    smallest_difference = abs(
        best_workout.total_distance - state.distance_goal
    )

    for workout in matching_workouts:

        difference = abs(
            workout.total_distance - state.distance_goal
        )

        if difference < smallest_difference:
            best_workout = workout
            smallest_difference = difference

    return best_workout


# --------------------------------------------------
# ROUTE 1: HOME PAGE
# --------------------------------------------------

@route
def index(state: State) -> Page:
    """
    Main landing page for SwimSet.

    Introduces the application and provides navigation
    to the generator, workout library, favorites, and
    about page.
    """

    return Page(state, [
        Header("SWIMSET"),
        "Your next swim workout starts here.",
        HorizontalRule(),

        Header("Welcome to SwimSet!", 2),

        "Stop spending time planning your workouts.",

        "Choose your skill level, training focus, and "
        "distance goal to find a workout.",

        "\n",

        Button("Generate a Workout", "workout_generator"),

        Button("Explore Workout Library", "workout_library"),

        Button("My Favorite Workouts", "favorites"),

        Button("About SwimSet", "about")
    ])


# --------------------------------------------------
# ROUTE 2: WORKOUT GENERATOR
# --------------------------------------------------

@route
def workout_generator(state: State) -> Page:
    """
    Displays the form where users enter their workout
    preferences.
    """

    return Page(state, [
        Header("Workout Generator"),

        "Customize your next swimming workout!",

        HorizontalRule(),

        Header("1. Choose Your Skill Level", 3),

        SelectBox(
            "skill_level",
            ["Beginner", "Intermediate", "Advanced"],
            state.skill_level
        ),

        Header("2. Choose Your Workout Focus", 3),

        SelectBox(
            "workout_focus",
            [
                "Endurance",
                "Sprint",
                "Pace Training",
                "Technique",
                "Recovery"
            ],
            state.workout_focus
        ),

        Header("3. Enter Your Distance Goal", 3),

        "Enter your desired distance in yards:",

        TextBox("distance_goal", state.distance_goal),

        "\n",

        Button("Generate My Workout", "generate_workout"),

        Button("Back Home", "index")
    ])


# --------------------------------------------------
# ROUTE 3: GENERATE WORKOUT
# --------------------------------------------------

@route
def generate_workout(
    state: State,
    skill_level: str,
    workout_focus: str,
    distance_goal: int
) -> Page:
    """
    Processes the user's input and generates a workout.

    The selected preferences are saved in State.
    The helper function searches the library for the
    closest matching workout.
    """

    # Save the user's selections.
    state.skill_level = skill_level
    state.workout_focus = workout_focus
    state.distance_goal = distance_goal

    # Validate the distance.
    if distance_goal <= 0:
        return Page(state, [
            Header("Invalid Distance"),
            "Please enter a distance greater than zero.",
            Button("Try Again", "workout_generator")
        ])

    # Generate the workout.
    state.current_workout = find_workout(state)

    # Check whether a matching workout exists.
    if state.current_workout is None:
        return Page(state, [
            Header("No Workout Found"),
            "We couldn't find a matching workout.",
            Button("Try Again", "workout_generator")
        ])

    return view_workout(state)


# --------------------------------------------------
# ROUTE 4: VIEW GENERATED WORKOUT
# --------------------------------------------------

@route
def view_workout(state: State) -> Page:
    """
    Displays the generated workout.

    The warmup, main set, and cooldown are displayed
    separately so the swimmer can easily follow along.
    """

    if state.current_workout is None:
        return Page(state, [
            Header("No Workout Yet"),
            "Generate a workout to see it here.",
            Button("Workout Generator", "workout_generator")
        ])

    workout = state.current_workout

    return Page(state, [
        Header("Your Generated Workout"),

        Header(workout.name, 2),

        "Skill Level: " + workout.skill_level,

        "Workout Focus: " + workout.workout_focus,

        "Requested Distance: " + str(state.distance_goal)
        + " yards",

        "Workout Distance: " + str(workout.total_distance)
        + " yards",

        HorizontalRule(),

        Header("Warmup", 2),

        BulletedList(workout.warmup),

        Header("Main Set", 2),

        BulletedList(workout.main_set),

        Header("Cooldown", 2),

        BulletedList(workout.cooldown),

        HorizontalRule(),

        Button("Save to Favorites", "save_favorite"),

        Button("Generate Another Workout", "workout_generator"),

        Button("Back Home", "index")
    ])


# --------------------------------------------------
# ROUTE 5: WORKOUT LIBRARY
# --------------------------------------------------

@route
def workout_library(state: State) -> Page:
    """
    Displays every workout available in the library.

    A for loop iterates through the list of SwimSet
    instances and displays their names, skill levels,
    training focuses, and distances.
    """

    content = [
        Header("Workout Library"),

        "Explore the different workouts available.",

        HorizontalRule()
    ]

    # Loop through every workout in the library.
    for workout in state.workout_library:

        content.append(Header(workout.name, 3))

        content.append(
            "Skill Level: " + workout.skill_level
        )

        content.append(
            "Focus: " + workout.workout_focus
        )

        content.append(
            "Distance: " + str(workout.total_distance)
            + " yards"
        )

        content.append(
            Button(
                "View Workout",
                "view_library_set",
                [Argument(
                    "set_index",
                    state.workout_library.index(workout)
                )]
            )
        )

        content.append(HorizontalRule())

    content.append(Button("Back Home", "index"))

    return Page(state, content)


# --------------------------------------------------
# ROUTE 6: VIEW INDIVIDUAL LIBRARY WORKOUT
# --------------------------------------------------

@route
def view_library_set(
    state: State,
    set_index: int
) -> Page:
    """
    Displays the details of an individual workout
    selected from the workout library.

    The set_index parameter identifies which workout
    the user selected.
    """

    if set_index < 0 or set_index >= len(state.workout_library):
        return Page(state, [
            Header("Workout Not Found"),
            Button("Return to Library", "workout_library")
        ])

    workout = state.workout_library[set_index]

    return Page(state, [
        Header(workout.name),

        "Skill Level: " + workout.skill_level,

        "Focus: " + workout.workout_focus,

        "Total Distance: " + str(workout.total_distance)
        + " yards",

        HorizontalRule(),

        Header("Warmup", 2),

        BulletedList(workout.warmup),

        Header("Main Set", 2),

        BulletedList(workout.main_set),

        Header("Cooldown", 2),

        BulletedList(workout.cooldown),

        Button("Return to Library", "workout_library"),

        Button("Back Home", "index")
    ])


# --------------------------------------------------
# ROUTE 7: FAVORITES PAGE
# --------------------------------------------------

@route
def favorites(state: State) -> Page:
    """
    Displays all workouts saved by the user.

    A loop iterates through the favorite_workouts
    list and displays each saved SwimSet instance.
    """

    content = [
        Header("My Favorite Workouts"),

        "Your saved swimming workouts.",

        HorizontalRule()
    ]

    # Check whether the user has saved any workouts.
    if len(state.favorite_workouts) == 0:

        content.append("You haven't saved any workouts yet.")

    else:

        # Loop through saved workout instances.
        for workout in state.favorite_workouts:

            content.append(Header(workout.name, 3))

            content.append(
                "Focus: " + workout.workout_focus
            )

            content.append(
                "Distance: " + str(workout.total_distance)
                + " yards"
            )

            content.append(
                BulletedList(workout.main_set)
            )

            content.append(HorizontalRule())

    content.append(Button("Back Home", "index"))

    return Page(state, content)


# --------------------------------------------------
# ROUTE 8: SAVE FAVORITE
# --------------------------------------------------

@route
def save_favorite(state: State) -> Page:
    """
    Saves the currently generated workout to favorites.

    The function checks that a workout exists and
    prevents the same workout from being saved twice.
    """

    if state.current_workout is None:
        return Page(state, [
            Header("No Workout to Save"),
            Button("Generate Workout", "workout_generator")
        ])

    already_saved = False

    for workout in state.favorite_workouts:

        if workout.name == state.current_workout.name:
            already_saved = True

    if not already_saved:
        state.favorite_workouts.append(
            state.current_workout
        )

    return Page(state, [
        Header("Favorites Updated"),

        "Your workout has been saved!",

        Button("View Favorites", "favorites"),

        Button("Back to Workout", "view_workout"),

        Button("Back Home", "index")
    ])


# --------------------------------------------------
# ROUTE 9: ABOUT PAGE
# --------------------------------------------------

@route
def about(state: State) -> Page:
    """
    Explains the purpose of SwimSet and how the
    application generates swimming workouts.
    """

    return Page(state, [
        Header("About SwimSet"),

        "SwimSet was created to make planning swimming "
        "workouts easier.",

        HorizontalRule(),

        Header("How It Works", 2),

        "1. Select your swimming skill level.",

        "2. Choose a workout focus.",

        "3. Enter your desired workout distance.",

        "4. SwimSet searches its workout library.",

        "5. A matching workout is displayed.",

        HorizontalRule(),

        "The goal is to help swimmers spend less time "
        "planning workouts and more time swimming!",

        Button("Back Home", "index")
    ])


# --------------------------------------------------
# UNIT TESTS
# --------------------------------------------------

def test_find_workout():
    """
    Tests whether the workout generator can find
    a workout matching the selected preferences.
    """

    test_state = State(
        "Beginner",
        "Endurance",
        1200,
        None,
        [],
        create_workout_library()
    )

    workout = find_workout(test_state)

    assert workout is not None
    assert workout.skill_level == "Beginner"
    assert workout.workout_focus == "Endurance"


def test_save_favorite():
    """
    Tests whether a generated workout can be added
    to the favorites list.
    """

    library = create_workout_library()

    test_state = State(
        "Beginner",
        "Endurance",
        1200,
        library[0],
        [],
        library
    )

    save_favorite(test_state)

    assert len(test_state.favorite_workouts) == 1


# Run tests before starting the website.
test_find_workout()
test_save_favorite()


# --------------------------------------------------
# START WEBSITE
# --------------------------------------------------

start_server(
    State(
        "Beginner",
        "Endurance",
        1500,
        None,
        [],
        create_workout_library()
    ),
    site_title="SwimSet"
)
