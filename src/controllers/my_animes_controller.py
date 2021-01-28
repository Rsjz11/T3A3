from models.My_Anime import My_Anime
from models.Profile import Profile
from main import db
from flask import Blueprint, request, jsonify, abort, render_template
from schemas.My_AnimeSchema import My_Animes_schema, my_anime_schema
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from models.User import User
from sqlalchemy import text


journal = Blueprint("my_anime", __name__, url_prefix="/my_anime")


@my_anime.route("/", methods=["GET"])
@jwt_required
def get_anime_titles():                                                                     # Return all anime titles for a profile
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid profile")

    animes = My_Anime.query.filter_by(profile_id_fk=user.id).all()
    # return jsonify(my_animes_schema.dump(animes))
    return render_template("My_Anime.html", animes=animes)

@my_anime.route("/recent", methods=["GET"])
@jwt_required
def get_recently_watched_anime():                                                             # Returns most recently watched anime
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid profile")

    animes = My_Anime.query.filter_by(profile_id_fk=user.id).order_by(My_Anime.anime_started.desc()).limit(3).all()
    # return jsonify(my_animes_schema.dump(animes))
    return render_template("My_Anime.html", animes=animes)


@my_anime.route("/", methods=["POST"])
@jwt_required
def anime_title_create():                                                                    # Create a anime entry
    user_id = get_jwt_identity()
    user = Profile.query.get(user_id)
    if not user:
        return abort(401, description="Invalid profile")

    anime_fields = my_anime_schema.load(request.json)
    new_anime = Anime()
    new_anime.anime_title = anime_fields["anime_title"]

    user.anime_titles.append(new_anime)

    db.session.add(new_anime)
    db.session.commit()

   # return jsonify(my_anime_schema.dump(new_anime))
    return render_template("My_Anime.html", new_anime=new_anime)

@my_anime.route("/<int:id>", methods=["GET"])
@jwt_required
def get_anime_title_show(id):                                                                    # Returns a single anime title
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid profile")

    animes = Anime.query.filter_by(id=id, profile_id_fk=user.id).first()
    # return jsonify(my_anime_schema.dump(animes))
    return render_template("My_Anime.html", animes=animes)

@my_anime.route("/<int:year>/<int:month>/<int:day>", methods=["GET"])                       # Returns anime entries for a selected date
@jwt_required
def get_anime_title_date(year, month, day):
    user_id = get_jwt_identity()
    user = Client.query.get(user_id)
    if not user:
        return abort(401, description="Invalid profile")

    result = Anime.date_filter(year, month, day, user.id)
    result_as_list = result.fetchall()

    anime_list = []
    for title in result_as_list:
        anime_list.append({"id": title.id, "anime_title": title.anime_title})
    return jsonify(anime_list)


@my_anime.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
def anime_title_update(id):                                                                     # Update a journal entry
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid profile")

    anime = My_Anime.query.filter_by(id=id, profile_id_fk=user.id)
    anime_fields = my_anime_schema.load(request.json)
    anime.update(anime_fields)
    db.session.commit()
    return jsonify(my_anime_schema.dump(anime[0]))


@my_anime.route("/<int:id>", methods=["DELETE"])
@jwt_required
def anime_title_delete(id):                                                                     # delete a anime title
    user_id = get_jwt_identity()
    user = Profile.query.get(user_id)
    if not user:
        return abort(401, description="Invalid profile")
    anime = My_anime.query.filter_by(id=id, profile_id_fk=user.id).first()
    print(My_Anime)
    if not My_Anime:
        return "deleted"
    db.session.delete(My_Anime)
    db.session.commit()

    # return jsonify(My_Anime_schema.dump(My_Anime))
    return render_template("My_Anime.html", My_Anime=My_Anime