from .models import prisma

async def seed_data():
    # Example of adding seed data
    await prisma.user.create(
        data={
            "name": "Admin User",
            "email": "admin@example.com"
        }
    )

# Example of running the seeding function
if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_data())
