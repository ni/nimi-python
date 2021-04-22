import typing

# Common
EmptyMapping = typing.MutableMapping[typing.Any, typing.Any]
Table = typing.Sequence[typing.Sequence[str]]
Documentation = typing.MutableMapping[str, typing.Union[str, typing.Sequence[str], Table, EmptyMapping]]

# Attributes
Attribute = typing.MutableMapping[str, typing.Union[str, bool, None, Documentation]]
Attributes = typing.MutableMapping[int, Attribute]

# Functions
Size = typing.MutableMapping[str, typing.Union[str, int, object]]
SizeStrOnly = typing.MutableMapping[str, str]
Parameter = typing.MutableMapping[str, typing.Union[str, bool, None, Documentation, Size, SizeStrOnly]]
Parameters = typing.Sequence[typing.Any]
MethodTemplate = typing.MutableMapping[str, str]
MethodTemplates = typing.Sequence[MethodTemplate]
Function = typing.MutableMapping[str, typing.Union[str, bool, Documentation, Parameters, MethodTemplates]]
Functions = typing.MutableMapping[str, Function]

# Enums
Value = typing.MutableMapping[str, typing.Union[Documentation, str, int]]
Values = typing.Sequence[Value]
Enum = typing.MutableMapping[str, typing.Union[str, Values]]
Enums = typing.MutableMapping[str, Enum]

# Config
OS = typing.MutableMapping[str, typing.MutableMapping[str, typing.MutableMapping[str, str]]]
ContextManager = typing.MutableMapping[str, str]
CustomType = typing.MutableMapping[str, str]
CustomTypes = typing.Sequence[CustomType]
WhiteListSuffix = typing.Optional[typing.Sequence[str]]
# Modules is only used during merging
Modules = typing.MutableMapping[str, typing.Any]
Config = typing.MutableMapping[str, typing.Union[str, bool, OS, ContextManager, CustomTypes, WhiteListSuffix, Modules, Attributes, Functions, Enums, EmptyMapping]]


