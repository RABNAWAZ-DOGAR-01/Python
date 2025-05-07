def settings(**options):
    theme = options.get("theme", "Light Mode")
    language = options.get("language", "English")
    
    print(f"Theme: {theme}, Language: {language}")

settings(theme="Dark Mode", language="Urdu")
settings()
