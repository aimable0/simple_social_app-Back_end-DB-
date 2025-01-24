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
class Users(Base):
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

# add a user record to the database
# add_user("Jeanluc", "Nkurikiye", "@jeanlu", "jeanluc@gmail.com", Session)

# add a post record to the database
# user_id = "6f77faba-1c02-44dc-9935-d76626d13f9c"
# add_post(user_id, "How have studying at KSS been for me, not what you expect!@..", Session)

# all_posts = (
#     Session()
#     .query(Posts)
#     .filter(Posts.userId == "6f77faba-1c02-44dc-9935-d76626d13f9c")
#     .all()
# )
# posts_ = [post.post_content for post in all_posts]
# print(posts_)
# for post in all_posts:
#     print(post.post_content)

# like post..
user_id = "6f77faba-1c02-44dc-9935-d76626d13f9c"
post_id = "4a56d213-4cc7-45ee-88d1-d92ed4cf0206"
like_post(user_id, post_id, Session)

#trying to retrieve a like id
likes  = Session().query(Likes).filter(Likes.post_id == "4a56d213-4cc7-45ee-88d1-d92ed4cf0206").count()
print(f"this post (4a56d213-4cc7-45ee-88d1-d92ed4cf0206) has {likes} likes")