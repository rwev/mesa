# `mesa` 

`mesa` is a [brutalist](https://brutalist-web.design/), [coyote](https://gitlab.com/rwev/pypalette.git) theme for Python-based [Pelican](https://getpelican.com) static site generator. 

See my personal blog [coyote.life](https://coyote.life) to see `mesa` in action.

## configuration

This repository includes [`mesaconf.py`](https://gitlab.com/rwev/mesa/blob/master/mesaconf.py) where default theme configuration is stored. 

Import the configuration from `mesaconf.py` into your site's `pelicanconf.py` to  provide them to the Pelican's generation context. Assuming this repository in cloned and in your site's directory:
 
 ```[python]
# pelicanconf.py
sys.path.append(os.curdir)
from mesa import *
```

Overwrite any of the variables in your `pelicanconf.py` after this import, whether they be static template display strings or plugin configuration.
 
 See the example [`pelicanconf.py`](https://gitlab.com/rwev/coyote.life/blob/master/pelicanconf.py) as reference.
 
## plugin support

`mesa`'s templates and base configuration support the following plugins out of the box:

- [autopages](https://github.com/getpelican/pelican-plugins/tree/master/autopages)
- [similar_posts](https://github.com/davidlesieur/similar_posts/tree/d6014555961f931d0a1b8c4e90e3fdb3439e6300)
- [neighbors](https://github.com/getpelican/pelican-plugins/tree/master/neighbors)
- [more_categories](https://github.com/getpelican/pelican-plugins/tree/master/more_categories)
- [photos](https://github.com/getpelican/pelican-plugins/tree/master/photos)
- [summary](https://github.com/getpelican/pelican-plugins/tree/master/summary)
- [clean_summary](https://github.com/getpelican/pelican-plugins/tree/master/summary)

