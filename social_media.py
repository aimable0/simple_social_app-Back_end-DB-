# creating simple database for simple social network backend

from sqlalchemy import create_engine, ForeignKey, String, Integer, Column
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import uuid

Base = declarative_base()


# function for generating random unique ids
def generate_uuid():
    return str(uuid.uuid4())


# User class: for creating a user record in the database
class Users(Base):
    __tablename__ = "users"
    userID = Column(
        "userID", String, primary_key=True, default=generate_uuid, nullable=False
    )
    first_name = Column("first_name", String, nullable=False)
    last_name = Column("last_name", String, nullable=False)
    profile_name = Column("profile_name", String, nullable=False)
    email = Column(String, nullable=True)

    def __init__(self, first_name, last_name, profile_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.profile_name = profile_name
        self.email = email

    def __str__(self):
        return (
            f"{self.first_name} + {self.last_name} + {self.profile_name} + {self.email}"
        )


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


# Likes class: for liking a post
class Likes(Base):
    __tablename__ = "likes"
    likeId = Column(
        "likeId", String, primary_key=True, default=generate_uuid, nullable=False
    )
    userId = Column("userId", String, ForeignKey("users.userID"), nullable=False)
    post_id = Column("post_id", String, ForeignKey("posts.post_id"), nullable=False)

    def __init__(self, userId, post_id):
        self.userId = userId
        self.post_id = post_id


# function for adding a user to the database
def add_user(first_name, last_name, profile_name, email, Session):
    with Session() as session:
        # check for existing users
        if session.query(Users).filter(Users.email == email).all():
            print("User with that email already exists!")
        else:
            user = Users(first_name, last_name, profile_name, email)
            session.add(user)
            session.commit()


# function for adding a post to the database
def add_post(user_id, post_content, Session):
    with Session() as session:
        post = Posts(user_id, post_content)
        session.add(post)
        session.commit()


# liking a post
def like_post(user_id, post_id, Session):
    with Session() as session:
        # check if post already like by the same person
        # post_liked  = session.query().join

        like = Likes(user_id, post_id)
        session.add(like)
        session.commit()
        print("like was added!")


# creating sqlite db
db = "sqlite:///socialDB.db"  # database path
engine = create_engine(db, echo=False)
Base.metadata.create_all(bind=engine)

# creating a session
Session = sessionmaker(bind=engine)

# add_user("Didier", "Muhire", "@didos", "didier@gmail.com", Session)

# Users: 6
# Likes: 9
# Posts: 9

# try querying some data..
session = Session()
# objs = [Users, Likes, Posts]
# i = 1
# obj_dict = {}
# for table in objs:
#     for obj in session.query(table):
#         obj_dict[obj.__class__.__name__] = obj

# for key, value in obj_dict.items():
#     print(key, value)

user_dict = {}
for obj in session.query(Users):
    user_dict[f"{obj.__class__.__name__}.{obj.userID}"] = obj

for key, value in user_dict.items():
    print(key, ':', value)

session.delete()