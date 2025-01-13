def headline(title: str, show: bool = True) -> str:
    if(show==True):
        return f"headline is {title}"
    else:
        return f'no headline should be shown'
    
print(headline(title="Hi AMRUTA", show=False))
print(headline(title="Hi AMRUTA, welcome to this page",))
