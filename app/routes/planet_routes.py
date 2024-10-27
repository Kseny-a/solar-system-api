from flask import Blueprint, abort, make_response
from app.models.planet import Planet

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

# @planets_bp.get("")
# def get_all_planets():
#     results_list = []

#     for planet in planets:
#         results_list.append(dict(
#             id=planet.id, 
#             name=planet.name,
#             description=planet.description,
#             num_moon=planet.num_moons
#         ))

#     return results_list

# @planets_bp.get("/<planet_id>")
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)
#     return planet.to_dict(), 200


# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message": f"Planet {planet_id} is invalid."}, 400))
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
#     abort(make_response({"message": f"Planet {planet_id} is not found."}, 404))    