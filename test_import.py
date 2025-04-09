try:
    import platipath
    print("Successfully imported platipath!")
    print(f"Package location: {platipath.__file__}")
except ImportError as e:
    print(f"Failed to import platipath: {e}")
