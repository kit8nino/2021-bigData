f :: Fractional a => a -> a
f x = x^3 + 0.3*x^2 + 4.5*x + 1.1

deriv :: Fractional a => a -> a
deriv = recip . (\x -> 3*x^2 + 0.6*x + 4.5)

g' :: Fractional a => a -> a -> a
g' x0 x = x - deriv x0 * f x

g :: Double -> Double
g = g' 0.1


simple_iter :: (Ord t, Num t, Fractional t) => (t -> t) -> t -> t -> t
simple_iter f x e
    | sub < e = x
    | otherwise = simple_iter f res e
    where sub = abs (res - x)
          res = f x

main = do
    presition <- getLine
    let res = simple_iter g 0.1 (read  presition)
    print res
