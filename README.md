Takeaways
Migrations

-encapsulate a set of changes to our database schema, made over time.
-are uniquely named
-are usually stored as local files in our project repo, e.g. a migrations/ folder
-There should be a 1-1 mapping between the changes made to our database, and the migration files that exist in our migrations/ folder.
-Our migrations files set up the tables for our database.
-All changes made to our db should exist physically as part of migration files in our repository.
Migration command line scripts
There are generally 3 scripts needed, for

migrate: creating a migration script template to fill out; generating a migration file based on changes to be made
upgrade: applying migrations that hadn't been applied yet ("upgrading" our database)
downgrade: rolling back applied migrations that were problematic ("downgrading" our database)
Migration library for Flask + SQLAlchemy
Flask-Migrate is our library for migrating changes using SQLAlchemy. It uses a library called Alembic underneath the hood.
Flask-Migrate & Flask-Script
Flask-Migrate (flask_migrate) is our migration manager for migrating SQLALchemy-based database changes

Flask-Script (flask_script) lets us run migration scripts we defined, from the terminal

Steps to get migrations going
Initialize the migration repository structure for storing migrations
Create a migration script (using Flask-Migrate)
(Manually) Run the migration script (using Flask-Script)
Resources
Flask-Migrate docs
Why use migrations?
To see why migrations are useful, let's go through a concrete example with the to-do app.


Takeaways
Without migrations:

We do heavy-handed work, creating and recreating the same tables in our database even for minor changes
We can lose existing data in older tables we dropped
With migrations:

Auto-detects changes from the old version & new version of the SQLAlchemy models
Creates a migration script that resolves differences between the old & new versions
Gives fine-grain control to change existing tables
This is much better, because

We can keep existing schema structures, only modifying what needs to be modified
We can keep existing data
We isolate units of change in migration scripts that we can roll back to a “safe” db state

Takeaways
Overall Steps to Set Up & Run Migrations
Bootstrap database migrate commands: link to the Flask app models and database, link to command line scripts for running migrations, set up folders to store migrations (as versions of the database)
Run initial migration to create tables for SQLAlchemy models, recording the initial schema: ala git init && first git commit. Replaces use of db.create_all()
Migrate on changes to our data models
Make changes to the SQLAlchemy models
Allow Flask-Migrate to auto-generate a migration script based on the changes
Fine-tune the migration scripts
Run the migration, aka “upgrade” the database schema by a “version”
It’s always helpful to read the docs!
https://alembic.sqlalchemy.org/en/latest/
https://flask-migrate.readthedocs.io/en/latest/