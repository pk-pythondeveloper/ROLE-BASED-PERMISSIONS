from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

#store referse token
class RefreshToken(Base):
    __tablename__ = "refresh_tokens"
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, index=True) 
    user_id = Column(Integer, ForeignKey("users.id"))
    users = relationship("User", back_populates="refresh_tokens")

# User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    roles = relationship("Role", secondary="user_role", back_populates="users")
    products = relationship("Product", back_populates="users") 
    refresh_tokens = relationship("RefreshToken", back_populates="users")

# Role model
class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    permissions = relationship("Permission", secondary="role_permissions", back_populates="roles")  # Fix here!
    users = relationship("User", secondary="user_role", back_populates="roles")
    role_permissions = relationship("RolePermission", back_populates="role")

class Permission(Base):
    __tablename__ = 'permissions'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    roles = relationship("Role", secondary="role_permissions", back_populates="permissions")  # Fix here!
    role_permissions = relationship("RolePermission", back_populates="permission")


# Many-to-many relationship tables
class UserRole(Base):
    __tablename__ = 'user_role'
    user_id = Column(Integer, ForeignKey('users.id',ondelete="CASCADE"), primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.id',ondelete="CASCADE"), primary_key=True)



class RolePermission(Base):
    __tablename__ = "role_permissions"
    id = Column(Integer, primary_key=True, index=True)
    role_id = Column(Integer, ForeignKey("roles.id",ondelete="CASCADE"), nullable=False)
    permission_id = Column(Integer, ForeignKey("permissions.id",ondelete="CASCADE"), nullable=False)  
    role = relationship("Role", back_populates="role_permissions")
    permission = relationship("Permission", back_populates="role_permissions")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id",ondelete="CASCADE"), nullable=False)
    users = relationship("User", back_populates="products")
