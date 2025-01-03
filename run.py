from flaskblog import app

if __name__ == '__main__':
    # with app.app_context():
        # db.create_all()
        # user_1 = User(username="a", email="a@gmail.com", password="a")
        # db.session.add(user_1)
        # user_2 = User(username="b", email="b@gmail.com", password="b")
        # db.session.add(user_2)
        # user_3 = User(username="c", email="c@gmail.com", password="c")
        # db.session.add(user_3)
        # db.session.commit()

        # print(User.query.all())
        # print(User.query.first())
        # user = User.query.filter_by(username="a").all()
        # print(user)
        # # print(user.id)
        # print(user)
        # user = User.query.get(1)  # -------------------------------------------------------------------------------
        # user = User.query.filter_by(username="a").first()
        # print(user.posts)

        # p1 = Post(title="Blog 1", content="First post Content!", user_id=user.id)
        # p2 = Post(title="Blog 2", content="Second post Content!", user_id=user.id)
        # db.session.add(p1)
        # db.session.add(p2)
        # db.session.commit()
        # print(user.posts)
        # for p in user.posts:
        #     print(p.title)

        # post = Post.query.first()
        # print(post)
        # print(post.author)
        # print(post.user_id)
        # db.drop_all()
        # db.create_all()
        # print(User.query.all())
        # print(Post.query.all())

    app.run(debug=True)
