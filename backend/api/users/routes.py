"""Users routes module
"""

from fastapi import APIRouter, Depends, HTTPException, status
from src.auth.dependency import AccessToken, RoleChecker
