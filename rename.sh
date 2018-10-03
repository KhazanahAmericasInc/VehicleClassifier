rm -Rf *.gif
rm -Rf *.ash

i=1
for f in *.jpg
do
  mv "$f" "${i}.jpg"
  i=$((i+1))
done

a=1
for f in *.jpeg
do
  mv "$f" "${a}.jpeg"
  a=$((a+1))
done

b=1
for f in *.png
do
  mv "$f" "${b}.png"
  b=$((b+1))
done
