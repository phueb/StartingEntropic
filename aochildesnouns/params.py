import attr
import itertools


class Conditions:
    """
    information editable by user, about IVs in all conditions.
    Used only to create instances of Params, one for each condition.
    """

    # auto-filled  (but placeholders must be present)
    auto = {
        'targets_control': [False],
        'age': [''],
        'direction': [''],
    }

    # user-filled
    user = {
        'punctuation': ['keep'],  #, 'remove', 'merge'],
        'lemmas': [False],
        'normalize_cols': [False],
        'targets_name': ['nouns-sing_and_plural'],  # TODO does effect hold when including plurals?  # 'sem-no_numbers_no_times',
        'tags': ['NN'],  # TODO test
    }

    ivs = {}
    ivs.update(auto)
    ivs.update(user)

    @classmethod
    def all(cls):
        """return a generator that yields instances of Params, one for each condition."""
        for vs in itertools.product(*cls.ivs.values()):
            kw = {k: v for k, v in zip(cls.ivs, vs)}
            params = Params(**kw)
            yield params


@attr.s
class Params:
    """Information used at runtime about Ivs in a single condition. Do not edit"""

    # auto-filled conditions
    targets_control = attr.ib(validator=attr.validators.instance_of(bool))
    age = attr.ib(validator=attr.validators.instance_of(str))
    direction = attr.ib(validator=attr.validators.instance_of(str))

    # user-filled conditions
    punctuation: bool = attr.ib(validator=attr.validators.instance_of(str))
    lemmas: str = attr.ib(validator=attr.validators.instance_of(bool))
    normalize_cols: str = attr.ib(validator=attr.validators.instance_of(bool))

    # data (this should only rarely change, if ever)
    corpus_name = attr.ib(default='childes-20210205')
    num_days = attr.ib(default=1000)  # age range in each age bin - there are always two bins
    targets_name = attr.ib(default='sem-no_numbers_no_times')
    tags = attr.ib(default={'NN', 'NNS'})
