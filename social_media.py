# creating simple database for simple social network backend
from sqlalchemy import create_engine, ForeignKey, String, Integer, Column

# declarative base: which we will use to create models or classes for our database
from sqlalchemy.orm import declarative_base

# importing session maker
from sqlalchemy.orm import sessionmaker
import uuid

Base = declarative_base()


# function for generating random unique ids
def generate_uuid():
    return str(uuid.uuid4())


# User class: for creating a user record in the database
class User(Base):
    __tablename__ = "users"
    userID = Column(
        "userID", String, primary_key=True, default=generate_uuid, nullable=False
    )
    first_name = Column("first_name", String, nullable=False)
    last_name = Column("last_name", String, nullable=False)
    profile_name = Column("profile_name", String, nullable=False)
    email = Column("email", String, nullable=True)

    def __init__(self, first_name, last_name, profile_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.profile_name = profile_name
        self.email = email


# Post class: for creating a post record
class Posts(Base):
    __tablename__ = "posts"

    post_iD = Column(
        "post_id", String, primary_key=True, default=generate_uuid, nullable=False
    )
    userId = Column("userId", ForeignKey("users.userID"), nullable=False)
    post_content = Column("post_content", String, nullable=False)

    def __init__(self, userId, post_content):
        self.userId = userId
        self.post_content = post_content


# function for adding a user to the database
def add_user(first_name, last_name, profile_name, email, Session):
    with Session() as session:
        user = User(first_name, last_name, profile_name, email)
        session.add(user)
        session.commit()


# function for adding a post to the database
def add_post(user_id, post_content, Session):
    with Session() as session:
        post = Posts(user_id, post_content)
        session.add(post)
        session.commit()


# creating sqlite db
db = "sqlite:///socialDB.db"
engine = create_engine(db, echo=True)
Base.metadata.create_all(bind=engine)

# creating a session
Session = sessionmaker(bind=engine)


# add a user record to the database
add_user("Jeanluc", "Nkurikiye", "@jeanlu", "jeanluc@gmail.com", Session)

# add a post record to the database
user_id = "sdf"
add_post(user_id, "I love doing wavumbuzi.. here is why..", Session)
