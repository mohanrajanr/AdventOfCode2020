import collections

file = open('21.txt')


class Dish(object):
    def __init__(self, ingredients=None, allergens=None):
        self.ingredients = ingredients
        self.allergens = allergens

    def __repr__(self):
        return "\nIngredients:{}\nAllergens:{}\n".format(self.ingredients, self.allergens)

    def __cmp__(self, other):
        if len(self.allergens) < len(other.allergens):
            return -1
        elif len(self.allergens) == len(other.allergens):
            if len(self.ingredients) < len(other.ingredients):
                return -1
            elif len(self.ingredients) == len(other.ingredients):
                return 0
            else:
                return 1
        else:
            return 1

dishes = list()
ingredients = set()
allergens = set()
allergen_dishes = collections.defaultdict(list)

for line in file.readlines():
    splitted = line.split("(")
    ings = [ing.strip() for ing in splitted[0].split(" ") if ing]
    algns = [alg.strip() for alg in splitted[1].replace("contains", "").replace(")", "").split(",") if alg]

    dish = Dish(ings, algns)
    dishes.append(dish)

    ingredients.update(set(ings))
    allergens.update(set(algns))

    for algn in algns:
        allergen_dishes[algn].append(dish)


ingredient_allergen = {ing: '' for ing in ingredients}
allergen_ingredient = {algn: '' for algn in allergens}


def is_safe(allergen, ingredient):

    dishes = allergen_dishes[allergen]
    for dish in dishes:
        if ingredient not in dish.ingredients:
            return False
    return True


def do_bt(level):

    ing_values = allergen_ingredient.values()
    if len([val for val in ing_values if val == '']) == 0:
        return True

    for key, value in allergen_ingredient.items():

        if value != '':
            continue

        for ingred in ingredients:

            if ingred in ing_values:
                continue

            # print("Trying:{} for {} {}".format(ingred, key, level))
            if is_safe(key, ingred):
                # print("Safe:{} for {} {}".format(ingred, key, level))
                allergen_ingredient[key] = ingred

                if do_bt(level+1):
                    return True

                allergen_ingredient[key] = ''
            # print("Invalid:{} for {} {}".format(ingred, key, level))

# Part 1
do_bt(0)
print(allergen_ingredient)
all_free = set(ing for ing in ingredients if ing not in allergen_ingredient.values())
total = 0
for dish in dishes:
    for ing in dish.ingredients:
        if ing in all_free:
            total += 1
print("Part1 :{}".format(total))

sorted_keys = sorted(allergen_ingredient.keys())
print("Part2 :{}".format(','.join([allergen_ingredient[key] for key in sorted_keys])))
