# PRACTICE PROJECT: Contact Book
# Demonstrates: File I/O, JSON, OOP, Regex for validation, Exception handling

import json
import re
import os
from datetime import datetime
from abc import ABC, abstractmethod

# ============================================================================
# EXCEPTIONS
# ============================================================================

class ContactError(Exception):
    """Base exception for contact operations"""
    pass

class ContactNotFoundError(ContactError):
    """Contact not found"""
    def __init__(self, identifier):
        super().__init__(f"Contact not found: {identifier}")

class DuplicateContactError(ContactError):
    """Duplicate contact"""
    def __init__(self, identifier):
        super().__init__(f"Contact already exists: {identifier}")

class ValidationError(ContactError):
    """Validation error"""
    pass

# ============================================================================
# VALIDATORS
# ============================================================================

class Validator(ABC):
    """Abstract validator"""
    
    @abstractmethod
    def validate(self, value):
        """Return True if valid, raise ValidationError if not"""
        pass

class PhoneValidator(Validator):
    """Validate phone numbers"""
    
    # Matches: +1-234-567-8900, (123) 456-7890, 123-456-7890, 1234567890
    PATTERN = re.compile(
        r'^[\+]?[(]?[0-9]{1,3}[)]?[-\s\.]?'
        r'[(]?[0-9]{1,4}[)]?[-\s\.]?'
        r'[0-9]{1,4}[-\s\.]?[0-9]{1,9}$'
    )
    
    def validate(self, value):
        if not value:
            return True  # Optional field
        
        # Remove common formatting
        cleaned = re.sub(r'[\s\-\.\(\)]', '', value)
        
        if not re.match(r'^[\+]?[0-9]{7,15}$', cleaned):
            raise ValidationError(f"Invalid phone number: {value}")
        return True

class EmailValidator(Validator):
    """Validate email addresses"""
    
    PATTERN = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
    
    def validate(self, value):
        if not value:
            return True  # Optional field
        
        if not self.PATTERN.match(value):
            raise ValidationError(f"Invalid email: {value}")
        return True

class NameValidator(Validator):
    """Validate names"""
    
    def validate(self, value):
        if not value or len(value.strip()) < 1:
            raise ValidationError("Name is required")
        if len(value) > 100:
            raise ValidationError("Name is too long (max 100 characters)")
        return True

# ============================================================================
# CONTACT MODEL
# ============================================================================

class Contact:
    """Contact model with validation"""
    
    # Validators
    _name_validator = NameValidator()
    _phone_validator = PhoneValidator()
    _email_validator = EmailValidator()
    
    def __init__(self, name, phone="", email="", address="", 
                 birthday="", notes="", favorite=False, tags=None):
        self._id = None
        self._name = None
        self._phone = ""
        self._email = ""
        self._address = ""
        self._birthday = ""
        self._notes = ""
        self._favorite = False
        self._tags = []
        self._created_at = datetime.now()
        self._updated_at = datetime.now()
        
        # Set values with validation
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.birthday = birthday
        self.notes = notes
        self.favorite = favorite
        self.tags = tags or []
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name_validator.validate(value)
        self._name = value.strip().title()
        self._touch()
    
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, value):
        self._phone_validator.validate(value)
        self._phone = value.strip()
        self._touch()
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        self._email_validator.validate(value)
        self._email = value.strip().lower()
        self._touch()
    
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, value):
        self._address = value.strip()
        self._touch()
    
    @property
    def birthday(self):
        return self._birthday
    
    @birthday.setter
    def birthday(self, value):
        self._birthday = value.strip()
        self._touch()
    
    @property
    def notes(self):
        return self._notes
    
    @notes.setter
    def notes(self, value):
        self._notes = value.strip()
        self._touch()
    
    @property
    def favorite(self):
        return self._favorite
    
    @favorite.setter
    def favorite(self, value):
        self._favorite = bool(value)
        self._touch()
    
    @property
    def tags(self):
        return self._tags.copy()
    
    @tags.setter
    def tags(self, value):
        if value:
            self._tags = [str(t).strip().lower() for t in value]
        else:
            self._tags = []
        self._touch()
    
    def add_tag(self, tag):
        """Add a tag"""
        tag = str(tag).strip().lower()
        if tag and tag not in self._tags:
            self._tags.append(tag)
            self._touch()
    
    def remove_tag(self, tag):
        """Remove a tag"""
        tag = str(tag).strip().lower()
        if tag in self._tags:
            self._tags.remove(tag)
            self._touch()
    
    def _touch(self):
        """Update the modified timestamp"""
        self._updated_at = datetime.now()
    
    def matches(self, query):
        """Check if contact matches search query"""
        query = query.lower()
        return (
            query in self._name.lower() or
            query in self._phone.lower() or
            query in self._email.lower() or
            query in self._address.lower() or
            query in self._notes.lower() or
            any(query in tag for tag in self._tags)
        )
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self._id,
            'name': self._name,
            'phone': self._phone,
            'email': self._email,
            'address': self._address,
            'birthday': self._birthday,
            'notes': self._notes,
            'favorite': self._favorite,
            'tags': self._tags,
            'created_at': self._created_at.isoformat(),
            'updated_at': self._updated_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create contact from dictionary"""
        contact = cls(
            name=data['name'],
            phone=data.get('phone', ''),
            email=data.get('email', ''),
            address=data.get('address', ''),
            birthday=data.get('birthday', ''),
            notes=data.get('notes', ''),
            favorite=data.get('favorite', False),
            tags=data.get('tags', [])
        )
        contact._id = data.get('id')
        if 'created_at' in data:
            contact._created_at = datetime.fromisoformat(data['created_at'])
        if 'updated_at' in data:
            contact._updated_at = datetime.fromisoformat(data['updated_at'])
        return contact
    
    def __str__(self):
        fav = "★" if self._favorite else " "
        return f"{fav} {self._name}" + (f" <{self._phone}>" if self._phone else "")
    
    def __repr__(self):
        return f"Contact(name='{self._name}', phone='{self._phone}')"

# ============================================================================
# STORAGE
# ============================================================================

class ContactStorage:
    """JSON file storage for contacts"""
    
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self._next_id = 1
    
    def save(self, contacts):
        """Save contacts to file"""
        data = {
            'next_id': self._next_id,
            'contacts': [c.to_dict() for c in contacts]
        }
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def load(self):
        """Load contacts from file"""
        if not os.path.exists(self.filename):
            return []
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self._next_id = data.get('next_id', 1)
            contacts = []
            for item in data.get('contacts', []):
                try:
                    contact = Contact.from_dict(item)
                    contacts.append(contact)
                except (ValidationError, KeyError) as e:
                    print(f"Warning: Could not load contact: {e}")
            
            return contacts
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load contacts file: {e}")
            return []
    
    def get_next_id(self):
        """Get next available ID"""
        next_id = self._next_id
        self._next_id += 1
        return next_id
    
    def export_csv(self, contacts, filename='contacts_export.csv'):
        """Export contacts to CSV"""
        import csv
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Phone', 'Email', 'Address', 'Birthday', 'Notes', 'Favorite', 'Tags'])
            for c in contacts:
                writer.writerow([
                    c.name, c.phone, c.email, c.address,
                    c.birthday, c.notes, 'Yes' if c.favorite else 'No',
                    ', '.join(c.tags)
                ])
        return filename

# ============================================================================
# CONTACT BOOK MANAGER
# ============================================================================

class ContactBook:
    """Contact book manager"""
    
    def __init__(self, storage=None):
        self.storage = storage or ContactStorage()
        self.contacts = []
        self._load()
    
    def _load(self):
        """Load contacts from storage"""
        self.contacts = self.storage.load()
    
    def _save(self):
        """Save contacts to storage"""
        self.storage.save(self.contacts)
    
    def add(self, name, phone="", email="", **kwargs):
        """Add a new contact"""
        # Check for duplicate by name and phone
        for c in self.contacts:
            if c.name.lower() == name.lower():
                if phone and c.phone == phone:
                    raise DuplicateContactError(f"{name} ({phone})")
        
        contact = Contact(name, phone, email, **kwargs)
        contact._id = self.storage.get_next_id()
        self.contacts.append(contact)
        self._save()
        return contact
    
    def get(self, contact_id):
        """Get contact by ID"""
        for c in self.contacts:
            if c.id == contact_id:
                return c
        raise ContactNotFoundError(contact_id)
    
    def find_by_name(self, name):
        """Find contacts by name (partial match)"""
        name = name.lower()
        return [c for c in self.contacts if name in c.name.lower()]
    
    def update(self, contact_id, **kwargs):
        """Update a contact"""
        contact = self.get(contact_id)
        
        for field, value in kwargs.items():
            if hasattr(contact, field):
                setattr(contact, field, value)
        
        self._save()
        return contact
    
    def delete(self, contact_id):
        """Delete a contact"""
        contact = self.get(contact_id)
        self.contacts.remove(contact)
        self._save()
        return contact
    
    def search(self, query):
        """Search contacts"""
        return [c for c in self.contacts if c.matches(query)]
    
    def get_favorites(self):
        """Get favorite contacts"""
        return [c for c in self.contacts if c.favorite]
    
    def get_by_tag(self, tag):
        """Get contacts by tag"""
        tag = tag.lower()
        return [c for c in self.contacts if tag in c.tags]
    
    def get_all(self, sort_by='name'):
        """Get all contacts sorted"""
        if sort_by == 'name':
            return sorted(self.contacts, key=lambda c: c.name.lower())
        elif sort_by == 'recent':
            return sorted(self.contacts, key=lambda c: c._updated_at, reverse=True)
        return self.contacts.copy()
    
    def get_all_tags(self):
        """Get all unique tags"""
        tags = set()
        for c in self.contacts:
            tags.update(c.tags)
        return sorted(tags)
    
    @property
    def count(self):
        """Get contact count"""
        return len(self.contacts)
    
    def export(self, filename='contacts_export.csv'):
        """Export contacts to CSV"""
        return self.storage.export_csv(self.contacts, filename)

# ============================================================================
# CLI INTERFACE
# ============================================================================

class ContactBookCLI:
    """Command-line interface for contact book"""
    
    def __init__(self, book):
        self.book = book
        self.commands = {
            '1': ('List all contacts', self.list_contacts),
            '2': ('Add new contact', self.add_contact),
            '3': ('View contact details', self.view_contact),
            '4': ('Edit contact', self.edit_contact),
            '5': ('Delete contact', self.delete_contact),
            '6': ('Search contacts', self.search_contacts),
            '7': ('View favorites', self.view_favorites),
            '8': ('Toggle favorite', self.toggle_favorite),
            '9': ('Manage tags', self.manage_tags),
            '10': ('Export to CSV', self.export_contacts),
            '0': ('Exit', None)
        }
    
    def run(self):
        """Run the CLI"""
        print("\n" + "=" * 60)
        print("📒 CONTACT BOOK")
        print("=" * 60)
        
        while True:
            print(f"\n📊 Total contacts: {self.book.count}")
            print("\n📋 MENU:")
            for key, (desc, _) in self.commands.items():
                print(f"  {key}. {desc}")
            
            choice = input("\nEnter choice: ").strip()
            
            if choice == '0':
                print("\n👋 Goodbye!")
                break
            
            if choice in self.commands:
                _, action = self.commands[choice]
                if action:
                    try:
                        action()
                    except ContactError as e:
                        print(f"\n❌ Error: {e}")
                    except ValidationError as e:
                        print(f"\n❌ Validation Error: {e}")
            else:
                print("\n❌ Invalid choice")
    
    def list_contacts(self):
        """List all contacts"""
        contacts = self.book.get_all()
        if not contacts:
            print("\n📭 No contacts yet")
            return
        
        print(f"\n📚 CONTACTS ({len(contacts)}):")
        print("-" * 50)
        for c in contacts:
            tags = f" [{', '.join(c.tags)}]" if c.tags else ""
            email = f" ({c.email})" if c.email else ""
            print(f"  [{c.id}] {c}{email}{tags}")
    
    def add_contact(self):
        """Add a new contact"""
        print("\n➕ ADD NEW CONTACT")
        print("(Press Enter to skip optional fields)")
        
        name = input("Name*: ").strip()
        if not name:
            print("❌ Name is required")
            return
        
        phone = input("Phone: ").strip()
        email = input("Email: ").strip()
        address = input("Address: ").strip()
        birthday = input("Birthday: ").strip()
        notes = input("Notes: ").strip()
        tags_input = input("Tags (comma-separated): ").strip()
        
        tags = [t.strip() for t in tags_input.split(',') if t.strip()] if tags_input else []
        
        contact = self.book.add(
            name=name,
            phone=phone,
            email=email,
            address=address,
            birthday=birthday,
            notes=notes,
            tags=tags
        )
        print(f"\n✅ Added: {contact}")
    
    def view_contact(self):
        """View contact details"""
        contact_id = self._get_contact_id()
        if contact_id is None:
            return
        
        contact = self.book.get(contact_id)
        
        print(f"\n👤 CONTACT DETAILS")
        print("=" * 40)
        print(f"ID: {contact.id}")
        print(f"Name: {contact.name}")
        print(f"Phone: {contact.phone or '(not set)'}")
        print(f"Email: {contact.email or '(not set)'}")
        print(f"Address: {contact.address or '(not set)'}")
        print(f"Birthday: {contact.birthday or '(not set)'}")
        print(f"Notes: {contact.notes or '(not set)'}")
        print(f"Favorite: {'Yes ★' if contact.favorite else 'No'}")
        print(f"Tags: {', '.join(contact.tags) if contact.tags else '(none)'}")
        print(f"Created: {contact._created_at.strftime('%Y-%m-%d %H:%M')}")
        print(f"Updated: {contact._updated_at.strftime('%Y-%m-%d %H:%M')}")
    
    def edit_contact(self):
        """Edit a contact"""
        contact_id = self._get_contact_id()
        if contact_id is None:
            return
        
        contact = self.book.get(contact_id)
        
        print(f"\n✏️ EDIT: {contact.name}")
        print("(Press Enter to keep current value)")
        
        updates = {}
        
        name = input(f"Name [{contact.name}]: ").strip()
        if name:
            updates['name'] = name
        
        phone = input(f"Phone [{contact.phone or 'none'}]: ").strip()
        if phone:
            updates['phone'] = phone
        
        email = input(f"Email [{contact.email or 'none'}]: ").strip()
        if email:
            updates['email'] = email
        
        address = input(f"Address [{contact.address or 'none'}]: ").strip()
        if address:
            updates['address'] = address
        
        birthday = input(f"Birthday [{contact.birthday or 'none'}]: ").strip()
        if birthday:
            updates['birthday'] = birthday
        
        notes = input(f"Notes [{contact.notes[:20] + '...' if len(contact.notes) > 20 else contact.notes or 'none'}]: ").strip()
        if notes:
            updates['notes'] = notes
        
        if updates:
            contact = self.book.update(contact_id, **updates)
            print(f"\n✅ Updated: {contact}")
        else:
            print("\n⚠️ No changes made")
    
    def delete_contact(self):
        """Delete a contact"""
        contact_id = self._get_contact_id()
        if contact_id is None:
            return
        
        contact = self.book.get(contact_id)
        
        confirm = input(f"Delete '{contact.name}'? (y/n): ").strip().lower()
        if confirm == 'y':
            self.book.delete(contact_id)
            print(f"\n✅ Deleted: {contact.name}")
        else:
            print("\n⚠️ Cancelled")
    
    def search_contacts(self):
        """Search contacts"""
        query = input("\n🔍 Search: ").strip()
        if not query:
            return
        
        results = self.book.search(query)
        
        if not results:
            print("\n📭 No results found")
        else:
            print(f"\n🔍 RESULTS ({len(results)}):")
            for c in results:
                print(f"  [{c.id}] {c}")
    
    def view_favorites(self):
        """View favorite contacts"""
        favorites = self.book.get_favorites()
        
        if not favorites:
            print("\n📭 No favorites yet")
            print("Use 'Toggle favorite' to add contacts to favorites")
        else:
            print(f"\n⭐ FAVORITES ({len(favorites)}):")
            for c in favorites:
                print(f"  [{c.id}] {c}")
    
    def toggle_favorite(self):
        """Toggle contact favorite status"""
        contact_id = self._get_contact_id()
        if contact_id is None:
            return
        
        contact = self.book.get(contact_id)
        new_status = not contact.favorite
        self.book.update(contact_id, favorite=new_status)
        
        if new_status:
            print(f"\n⭐ {contact.name} added to favorites")
        else:
            print(f"\n☆ {contact.name} removed from favorites")
    
    def manage_tags(self):
        """Manage contact tags"""
        print("\n🏷️ TAG MANAGEMENT")
        print("1. View all tags")
        print("2. View contacts by tag")
        print("3. Add tag to contact")
        print("4. Remove tag from contact")
        
        choice = input("\nChoice: ").strip()
        
        if choice == '1':
            tags = self.book.get_all_tags()
            if tags:
                print(f"\n🏷️ All tags: {', '.join(tags)}")
            else:
                print("\n📭 No tags yet")
        
        elif choice == '2':
            tag = input("Tag to search: ").strip()
            contacts = self.book.get_by_tag(tag)
            if contacts:
                print(f"\n🏷️ Contacts with '{tag}':")
                for c in contacts:
                    print(f"  [{c.id}] {c}")
            else:
                print(f"\n📭 No contacts with tag '{tag}'")
        
        elif choice == '3':
            contact_id = self._get_contact_id()
            if contact_id is None:
                return
            contact = self.book.get(contact_id)
            tag = input("Tag to add: ").strip()
            if tag:
                contact.add_tag(tag)
                self.book._save()
                print(f"\n✅ Added tag '{tag}' to {contact.name}")
        
        elif choice == '4':
            contact_id = self._get_contact_id()
            if contact_id is None:
                return
            contact = self.book.get(contact_id)
            if contact.tags:
                print(f"Current tags: {', '.join(contact.tags)}")
                tag = input("Tag to remove: ").strip()
                contact.remove_tag(tag)
                self.book._save()
                print(f"\n✅ Removed tag '{tag}' from {contact.name}")
            else:
                print("\n📭 Contact has no tags")
    
    def export_contacts(self):
        """Export contacts to CSV"""
        filename = input("Filename [contacts_export.csv]: ").strip()
        if not filename:
            filename = 'contacts_export.csv'
        
        result = self.book.export(filename)
        print(f"\n✅ Exported {self.book.count} contacts to {result}")
    
    def _get_contact_id(self):
        """Helper to get and validate contact ID"""
        try:
            contact_id = int(input("\nContact ID: ").strip())
            return contact_id
        except ValueError:
            print("❌ Invalid ID")
            return None

# ============================================================================
# DEMO
# ============================================================================

def demo():
    """Demonstrate contact book features"""
    print("📒 CONTACT BOOK - DEMO")
    print("=" * 60)
    
    # Use in-memory storage for demo
    class MemoryStorage:
        def __init__(self):
            self._next_id = 1
            self._data = []
        
        def save(self, contacts):
            self._data = [c.to_dict() for c in contacts]
        
        def load(self):
            return [Contact.from_dict(d) for d in self._data]
        
        def get_next_id(self):
            next_id = self._next_id
            self._next_id += 1
            return next_id
        
        def export_csv(self, contacts, filename):
            return filename
    
    book = ContactBook(MemoryStorage())
    
    # Add sample contacts
    print("\n📝 Adding contacts...")
    contacts_data = [
        {"name": "Alice Johnson", "phone": "+1-555-123-4567", "email": "alice@email.com", "tags": ["friend", "work"]},
        {"name": "Bob Smith", "phone": "+1-555-234-5678", "email": "bob.smith@company.com", "tags": ["work"]},
        {"name": "Charlie Brown", "phone": "+1-555-345-6789", "email": "charlie@mail.com", "tags": ["family"]},
        {"name": "Diana Ross", "phone": "+1-555-456-7890", "email": "diana@music.com", "tags": ["friend"]},
        {"name": "Eve Wilson", "phone": "+1-555-567-8901", "email": "eve.w@tech.io", "tags": ["work", "tech"]},
    ]
    
    for data in contacts_data:
        contact = book.add(**data)
        print(f"  Added: {contact}")
    
    # Set some favorites
    print("\n⭐ Setting favorites...")
    book.update(1, favorite=True)
    book.update(3, favorite=True)
    print("  Alice and Charlie marked as favorites")
    
    # List all contacts
    print(f"\n📚 All Contacts ({book.count}):")
    print("-" * 50)
    for c in book.get_all():
        fav = "★" if c.favorite else " "
        print(f"  [{c.id}] {fav} {c.name} <{c.phone}> - {c.email}")
    
    # Search
    print("\n🔍 Search 'alice':")
    for c in book.search("alice"):
        print(f"  {c}")
    
    # Favorites
    print("\n⭐ Favorites:")
    for c in book.get_favorites():
        print(f"  {c}")
    
    # Tags
    print("\n🏷️ All tags:", ", ".join(book.get_all_tags()))
    
    print("\n🏷️ Contacts with 'work' tag:")
    for c in book.get_by_tag("work"):
        print(f"  {c}")
    
    # View details
    print("\n👤 Contact Details (ID: 1):")
    contact = book.get(1)
    print(f"  Name: {contact.name}")
    print(f"  Phone: {contact.phone}")
    print(f"  Email: {contact.email}")
    print(f"  Tags: {', '.join(contact.tags)}")
    print(f"  Favorite: {'Yes' if contact.favorite else 'No'}")
    
    # Update
    print("\n✏️ Updating Eve's notes...")
    book.update(5, notes="Works at Tech Corp, expert in Python")
    print(f"  Updated: {book.get(5).notes}")
    
    # Validation demo
    print("\n🔍 Validation Examples:")
    
    # Invalid email
    try:
        book.add("Test User", email="invalid-email")
    except ValidationError as e:
        print(f"  ❌ {e}")
    
    # Invalid phone
    try:
        book.add("Test User", phone="abc")
    except ValidationError as e:
        print(f"  ❌ {e}")
    
    # Valid contact
    print("  ✅ Valid contact created successfully")
    book.add("Valid User", phone="+1-555-999-0000", email="valid@email.com")
    
    print("\n" + "=" * 60)
    print("✅ Demo complete!")
    print("=" * 60)

# Run
if __name__ == "__main__":
    print("\n1. Run Demo")
    print("2. Run Interactive CLI")
    choice = input("\nChoice (1/2): ").strip()
    
    if choice == "2":
        book = ContactBook()
        cli = ContactBookCLI(book)
        cli.run()
    else:
        demo()
