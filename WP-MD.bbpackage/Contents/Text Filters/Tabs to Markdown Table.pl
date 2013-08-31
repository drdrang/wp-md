#!/usr/bin/perl -p

# For each line...
$n = s/\t/\|/g;       # tabs to pipes, saving the count
s/^/\|/;              # pipe at beginning
s/$/\|/;              # pipe at end

# Add the formatting line above the second line.
printf "|" . "--|"x($n+1) . "\n" if $. == 2
