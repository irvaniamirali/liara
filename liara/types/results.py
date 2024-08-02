import json


class Results:

    def __str__(self) -> str:
        return self.jsonify(indent=2)

    def __getattr__(self, name):
        return self.find_keys(keys=name)

    def __setitem__(self, key, value):
        self.original_update[key] = value

    def __getitem__(self, key):
        return self.original_update[key]

    def __lts__(self, update: list, *args, **kwargs):
        for index, element in enumerate(update):
            if isinstance(element, list):
                update[index] = self.__lts__(update=element)
            elif isinstance(element, dict):
                update[index] = Results(update=element)
            else:
                update[index] = element
        return update

    def __init__(self, update: dict, *args, **kwargs) -> None:
        self.client = update.get("client")
        self.original_update = update

    def jsonify(self, indent=None) -> str:
        result = self.original_update
        result["original_update"] = "dict{...}"
        return json.dumps(result, indent=indent, ensure_ascii=False, default=lambda value: str(value))

    def find_keys(self, keys, original_update=None, *args, **kwargs):
        if original_update is None:
            original_update = self.original_update

        if not isinstance(keys, list):
            keys = [keys]

        if isinstance(original_update, dict):
            for key in keys:
                try:
                    update = original_update[key]
                    if isinstance(update, dict):
                        update = Results(update=update)
                    elif isinstance(update, list):
                        update = self.__lts__(update=update)
                    return update
                except KeyError:
                    pass
            original_update = original_update.values()

        for value in original_update:
            if isinstance(value, (dict, list)):
                try:
                    return self.find_keys(keys=keys, original_update=value)
                except AttributeError:
                    return None

        return None

    @property
    def to_dict(self) -> dict:
        """
        Return the update as dict
        """
        return self.original_update

    @property
    def user(self):
        return self.find_keys("user")

    @property
    def id(self):
        return self.user.find_keys("_id")

    @property
    def fullname(self):
        return self.user.find_keys("fullname")

    @property
    def national_code(self):
        return self.user.find_keys("nationalCode")

    @property
    def email(self):
        return self.user.find_keys("email")

    @property
    def phone(self):
        return self.user.find_keys("phone")

    @property
    def joined_at(self):
        return self.user.find_keys("joined_at")

    @property
    def free_credit_time(self):
        return self.user.find_keys("freeCreditTime")

    @property
    def remaining_free_credit(self):
        return self.user.find_keys("remainingFreeCredit")

    @property
    def balance(self):
        return self.user.find_keys("balance")

    @property
    def has_password(self):
        return self.user.find_keys("hasPassword")

    @property
    def min_credit_amount(self):
        return self.user.find_keys("minCreditAmount")

    @property
    def is_manual_min_credit(self):
        return self.user.find_keys("isManualMinCredit")

    @property
    def email_verified_at(self):
        return self.user.find_keys("emailVerifiedAt")

    @property
    def phone_verified_at(self):
        return self.user.find_keys("phoneVerifiedAt")

    @property
    def account_type(self):
        return self.user.find_keys("accountType")

    @property
    def is_verified(self):
        return self.user.find_keys("isVerified")

    @property
    def storage(self):
        return self.user.find_keys("storage")

    @property
    def storage_namespace(self):
        return self.storage.find_keys("namespace")

    @property
    def storage_status(self):
        return self.storage.find_keys("status")

    @property
    def avatar(self):
        return self.user.find_keys("avatar")

    @property
    def legacy_network_feature(self):
        return self.user.find_keys("legacyNetworkFeature")

    @property
    def private_network_feature(self):
        return self.user.find_keys("privateNetworkFeature")

    @property
    def legacy_object_storage_feature(self):
        return self.user.find_keys("legacyObjectStorageFeature")

    @property
    def legacy_domains_feature(self):
        return self.user.find_keys("legacyDomainsFeature")

    @property
    def current_subscription_plan(self):
        return self.user.find_keys("currentSubscriptionPlan")

    @property
    def database_versions(self):
        return self.find_keys("databaseVersions")

    @property
    def default_database_versions(self):
        return self.find_keys("defaultDatabaseVersions")

    @property
    def plans(self):
        return self.find_keys("plans")
