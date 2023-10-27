from django.shortcuts import render
from django.http.response import HttpResponse
from dataclasses import dataclass


@dataclass
class Team:
    name: str
    job: str
    members: list


teams_dict = {
    "procurement": Team(
        "Procurement",
        "Procurement team makes lunch everyday for Base Camp students. They also have to go out an buy/order the food that we eat.",
        [
            "Blaine",
            "Wyatt",
            "Adrian",
            "Johnathan",
            "Bryce",
        ],
    ),
    "community": Team(
        "Community",
        "Community team is in charge of planning bi-weekly events for everyone to participate in. Events are a good time for students to relax and bond.",
        ["Jordan", "Joby", "Caleb", "AJ", "Micah"],
    ),
    "documentation": Team(
        "Documentation",
        "Documentation team manages the Base Camp social media pages and take inventory of various things. This requires them to schedule, create, and post things to the social media like student interviews, community events, etc.",
        [
            "Joshua",
            "Kaleigh",
            "Mina",
            "Conner",
            "Jay",
            "Jeremiah",
        ],
    ),
    "management": Team(
        "Management",
        "Management team's duties consist of running stand ups, leading chores, and checks supplies.",
        ["Ab", "Matthew", "Kayleah", "Nick", "Blair", "Owen"],
    ),
}


def teams_view(request):
    return render(request, "teams.html", context={"team_names": teams_dict.keys()})


def team_detail_view(request, team_name):
    if team_name.lower() in teams_dict.keys():
        team = teams_dict[team_name.lower()]
        return render(
            request,
            "team_details.html",
            context={"team": teams_dict[team_name.lower()]},
        )

    else:
        return HttpResponse("<h1>" + team_name + " team not found. </h1>")
