db.createUser(
        {
            user: "root",
            pwd: "mongoadmin",
            roles: [
                {
                    role: "readWrite",
                    db: "django-test-demo"
                }
            ]
        }
);
