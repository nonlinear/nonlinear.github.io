## Requirements
- [Sublime Text](http://www.sublimetext.com) (2 or 3)
- [Animate.css SASS Mixins](https://github.com/geoffgraham/animate.scss)
- [nonlinear/snippets](https://github.com/nonlinear/snippets/#snippets)

## Animation Snippets (view animations at [Animate.css](https://daneden.github.io/animate.css/))

|type|snippets|
|---|---|
|attention seekers|`bounce` (new), `flash` (new), `jello` (new),`pulse`, `shake`, `swing`, `tada`, `wiggle`, `wobble`|
|bouncing|`bounce`, `bounceIn`, `bounceInDown`, `bounceInLeft`, `bounceInRight`, `bounceInUp`, `bounceOut`, `bounceOutDown`, `bounceOutLeft`, `bounceOutRight`, `bounceOutUp`|
|fading|`fadeIn`, `fadeInDown`, `fadeInDownBig`, `fadeInLeft`, `fadeInLeftBig`, `fadeInRight`, `fadeInRightBig`, `fadeInUp`, `fadeInUpBig`, `fadeOut`, `fadeOutDown`, `fadeOutDownBig`, `fadeOutLeft`, `fadeOutLeftBig`, `fadeOutRight`, `fadeOutRightBig`, `fadeOutUp`, `fadeOutUpBig`|
|flippers|`flip`, `flipInX`, `flipInY`, `flipOutX`, `flipOutY`|
|rotating|`rotateIn`, `rotateInDownLeft`, `rotateInDownRight`, `rotateInUpLeft`, `rotateInUpRight`, `rotateOut`, `rotateOutDownLeft`, `rotateOutDownRight`, `rotateOutUpLeft`, `rotateOutUpRight`|
|sliding|`slideInDown`, `slideInLeft`, `slideInRight`, `slideInUp`, `slideOutDown`, `slideOutLeft`, `slideOutRight`, `slideOutUp`|
|lightspeed|`lightSpeedIn`, `lightSpeedOut`|
|specials|`hinge` (new), `rollIn`, `rollOut`|
|zooming (new)|`zoomIn`, `zoomInDown`, `zoomInLeft`, `zoomInRight`, `zoomInUp`, `zoomOut`, `zoomOutDown`, `zoomOutLeft`, `zoomOutRight`, `zoomOutUp`|
|transform|animate`|`rotate`|`scale`|`skew`|`translate-01`(normal or 3D)|`variables`|

Variables are, in order:

- `$duration`
- `$function`
- `$delay`
- `$count`
- `$fill`
- `$visibility`

So if you want an object to bounce, `+bounce` will do it.

If you want it to bounce with a `300ms` delay, use `+bounce($delay: 300ms)`.

If you want it to also bounce 3 times, `+bounce($delay: 300ms, $count: 3)`, etc.

