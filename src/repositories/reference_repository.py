from config import db
from sqlalchemy import text


def create_reference(key, author, title, journal, year):
    sql = text(
        "INSERT INTO articles (key, author, title, journal, year) VALUES (:key, :author, :title, :journal, :year)"
    )
    db.session.execute(sql, {"key": key, "author": author,
                       "title": title, "journal": journal, "year": year})
    db.session.commit()
