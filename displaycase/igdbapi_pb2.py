# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: igdbapi.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rigdbapi.proto\x12\x05proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x16\n\x05\x43ount\x12\r\n\x05\x63ount\x18\x01 \x01(\x03\"@\n\x10MultiQueryResult\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07results\x18\x02 \x03(\x0c\x12\r\n\x05\x63ount\x18\x03 \x01(\x03\"@\n\x15MultiQueryResultArray\x12\'\n\x06result\x18\x01 \x03(\x0b\x32\x17.proto.MultiQueryResult\"7\n\x0f\x41geRatingResult\x12$\n\nageratings\x18\x01 \x03(\x0b\x32\x10.proto.AgeRating\"\xf3\x01\n\tAgeRating\x12\n\n\x02id\x18\x01 \x01(\x04\x12.\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\x1c.proto.AgeRatingCategoryEnum\x12@\n\x14\x63ontent_descriptions\x18\x03 \x03(\x0b\x32\".proto.AgeRatingContentDescription\x12*\n\x06rating\x18\x04 \x01(\x0e\x32\x1a.proto.AgeRatingRatingEnum\x12\x18\n\x10rating_cover_url\x18\x05 \x01(\t\x12\x10\n\x08synopsis\x18\x06 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x07 \x01(\t\"m\n!AgeRatingContentDescriptionResult\x12H\n\x1c\x61geratingcontentdescriptions\x18\x01 \x03(\x0b\x32\".proto.AgeRatingContentDescription\"~\n\x1b\x41geRatingContentDescription\x12\n\n\x02id\x18\x01 \x01(\x04\x12,\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\x1a.proto.AgeRatingRatingEnum\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x04 \x01(\t\"I\n\x15\x41lternativeNameResult\x12\x30\n\x10\x61lternativenames\x18\x01 \x03(\x0b\x32\x16.proto.AlternativeName\"i\n\x0f\x41lternativeName\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x12\x19\n\x04game\x18\x03 \x01(\x0b\x32\x0b.proto.Game\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x05 \x01(\t\"1\n\rArtworkResult\x12 \n\x08\x61rtworks\x18\x01 \x03(\x0b\x32\x0e.proto.Artwork\"\xa9\x01\n\x07\x41rtwork\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x15\n\ralpha_channel\x18\x02 \x01(\x08\x12\x10\n\x08\x61nimated\x18\x03 \x01(\x08\x12\x19\n\x04game\x18\x04 \x01(\x0b\x32\x0b.proto.Game\x12\x0e\n\x06height\x18\x05 \x01(\x05\x12\x10\n\x08image_id\x18\x06 \x01(\t\x12\x0b\n\x03url\x18\x07 \x01(\t\x12\r\n\x05width\x18\x08 \x01(\x05\x12\x10\n\x08\x63hecksum\x18\t \x01(\t\"7\n\x0f\x43haracterResult\x12$\n\ncharacters\x18\x01 \x03(\x0b\x32\x10.proto.Character\"\x89\x03\n\tCharacter\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04\x61kas\x18\x02 \x03(\t\x12\x14\n\x0c\x63ountry_name\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x1a\n\x05games\x18\x06 \x03(\x0b\x32\x0b.proto.Game\x12\'\n\x06gender\x18\x07 \x01(\x0e\x32\x17.proto.GenderGenderEnum\x12)\n\x08mug_shot\x18\x08 \x01(\x0b\x32\x17.proto.CharacterMugShot\x12\x0c\n\x04name\x18\t \x01(\t\x12\x0c\n\x04slug\x18\n \x01(\t\x12,\n\x07species\x18\x0b \x01(\x0e\x32\x1b.proto.CharacterSpeciesEnum\x12.\n\nupdated_at\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03url\x18\r \x01(\t\x12\x10\n\x08\x63hecksum\x18\x0e \x01(\t\"L\n\x16\x43haracterMugShotResult\x12\x32\n\x11\x63haractermugshots\x18\x01 \x03(\x0b\x32\x17.proto.CharacterMugShot\"\x97\x01\n\x10\x43haracterMugShot\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x15\n\ralpha_channel\x18\x02 \x01(\x08\x12\x10\n\x08\x61nimated\x18\x03 \x01(\x08\x12\x0e\n\x06height\x18\x04 \x01(\x05\x12\x10\n\x08image_id\x18\x05 \x01(\t\x12\x0b\n\x03url\x18\x06 \x01(\t\x12\r\n\x05width\x18\x07 \x01(\x05\x12\x10\n\x08\x63hecksum\x18\x08 \x01(\t\":\n\x10\x43ollectionResult\x12&\n\x0b\x63ollections\x18\x01 \x03(\x0b\x32\x11.proto.Collection\"\xcf\x01\n\nCollection\x12\n\n\x02id\x18\x01 \x01(\x04\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1a\n\x05games\x18\x03 \x03(\x0b\x32\x0b.proto.Game\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0c\n\x04slug\x18\x05 \x01(\t\x12.\n\nupdated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03url\x18\x07 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x08 \x01(\t\"2\n\rCompanyResult\x12!\n\tcompanies\x18\x01 \x03(\x0b\x32\x0e.proto.Company\"\x9b\x05\n\x07\x43ompany\x12\n\n\x02id\x18\x01 \x01(\x04\x12/\n\x0b\x63hange_date\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x45\n\x14\x63hange_date_category\x18\x03 \x01(\x0e\x32\'.proto.DateFormatChangeDateCategoryEnum\x12*\n\x12\x63hanged_company_id\x18\x04 \x01(\x0b\x32\x0e.proto.Company\x12\x0f\n\x07\x63ountry\x18\x05 \x01(\x05\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\x12\x1e\n\tdeveloped\x18\x08 \x03(\x0b\x32\x0b.proto.Game\x12 \n\x04logo\x18\t \x01(\x0b\x32\x12.proto.CompanyLogo\x12\x0c\n\x04name\x18\n \x01(\t\x12\x1e\n\x06parent\x18\x0b \x01(\x0b\x32\x0e.proto.Company\x12\x1e\n\tpublished\x18\x0c \x03(\x0b\x32\x0b.proto.Game\x12\x0c\n\x04slug\x18\r \x01(\t\x12.\n\nstart_date\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x44\n\x13start_date_category\x18\x0f \x01(\x0e\x32\'.proto.DateFormatChangeDateCategoryEnum\x12.\n\nupdated_at\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03url\x18\x11 \x01(\t\x12\'\n\x08websites\x18\x12 \x03(\x0b\x32\x15.proto.CompanyWebsite\x12\x10\n\x08\x63hecksum\x18\x13 \x01(\t\"=\n\x11\x43ompanyLogoResult\x12(\n\x0c\x63ompanylogos\x18\x01 \x03(\x0b\x32\x12.proto.CompanyLogo\"\x92\x01\n\x0b\x43ompanyLogo\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x15\n\ralpha_channel\x18\x02 \x01(\x08\x12\x10\n\x08\x61nimated\x18\x03 \x01(\x08\x12\x0e\n\x06height\x18\x04 \x01(\x05\x12\x10\n\x08image_id\x18\x05 \x01(\t\x12\x0b\n\x03url\x18\x06 \x01(\t\x12\r\n\x05width\x18\x07 \x01(\x05\x12\x10\n\x08\x63hecksum\x18\x08 \x01(\t\"F\n\x14\x43ompanyWebsiteResult\x12.\n\x0f\x63ompanywebsites\x18\x01 \x03(\x0b\x32\x15.proto.CompanyWebsite\"z\n\x0e\x43ompanyWebsite\x12\n\n\x02id\x18\x01 \x01(\x04\x12,\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\x1a.proto.WebsiteCategoryEnum\x12\x0f\n\x07trusted\x18\x03 \x01(\x08\x12\x0b\n\x03url\x18\x04 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x05 \x01(\t\"+\n\x0b\x43overResult\x12\x1c\n\x06\x63overs\x18\x01 \x03(\x0b\x32\x0c.proto.Cover\"\xa7\x01\n\x05\x43over\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x15\n\ralpha_channel\x18\x02 \x01(\x08\x12\x10\n\x08\x61nimated\x18\x03 \x01(\x08\x12\x19\n\x04game\x18\x04 \x01(\x0b\x32\x0b.proto.Game\x12\x0e\n\x06height\x18\x05 \x01(\x05\x12\x10\n\x08image_id\x18\x06 \x01(\t\x12\x0b\n\x03url\x18\x07 \x01(\t\x12\r\n\x05width\x18\x08 \x01(\x05\x12\x10\n\x08\x63hecksum\x18\t \x01(\t\"@\n\x12\x45xternalGameResult\x12*\n\rexternalgames\x18\x01 \x03(\x0b\x32\x13.proto.ExternalGame\"\xf3\x02\n\x0c\x45xternalGame\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x31\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\x1f.proto.ExternalGameCategoryEnum\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x19\n\x04game\x18\x04 \x01(\x0b\x32\x0b.proto.Game\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0b\n\x03uid\x18\x06 \x01(\t\x12.\n\nupdated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03url\x18\x08 \x01(\t\x12\x0c\n\x04year\x18\t \x01(\x05\x12+\n\x05media\x18\n \x01(\x0e\x32\x1c.proto.ExternalGameMediaEnum\x12!\n\x08platform\x18\x0b \x01(\x0b\x32\x0f.proto.Platform\x12\x11\n\tcountries\x18\x0c \x03(\x05\x12\x10\n\x08\x63hecksum\x18\r \x01(\t\"7\n\x0f\x46ranchiseResult\x12$\n\nfranchises\x18\x01 \x03(\x0b\x32\x10.proto.Franchise\"\xce\x01\n\tFranchise\x12\n\n\x02id\x18\x01 \x01(\x04\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1a\n\x05games\x18\x03 \x03(\x0b\x32\x0b.proto.Game\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0c\n\x04slug\x18\x05 \x01(\t\x12.\n\nupdated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03url\x18\x07 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x08 \x01(\t\"(\n\nGameResult\x12\x1a\n\x05games\x18\x01 \x03(\x0b\x32\x0b.proto.Game\"\xfd\r\n\x04Game\x12\n\n\x02id\x18\x01 \x01(\x04\x12%\n\x0b\x61ge_ratings\x18\x02 \x03(\x0b\x32\x10.proto.AgeRating\x12\x19\n\x11\x61ggregated_rating\x18\x03 \x01(\x01\x12\x1f\n\x17\x61ggregated_rating_count\x18\x04 \x01(\x05\x12\x31\n\x11\x61lternative_names\x18\x05 \x03(\x0b\x32\x16.proto.AlternativeName\x12 \n\x08\x61rtworks\x18\x06 \x03(\x0b\x32\x0e.proto.Artwork\x12\x1c\n\x07\x62undles\x18\x07 \x03(\x0b\x32\x0b.proto.Game\x12)\n\x08\x63\x61tegory\x18\x08 \x01(\x0e\x32\x17.proto.GameCategoryEnum\x12%\n\ncollection\x18\t \x01(\x0b\x32\x11.proto.Collection\x12\x1b\n\x05\x63over\x18\n \x01(\x0b\x32\x0c.proto.Cover\x12.\n\ncreated_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x19\n\x04\x64lcs\x18\x0c \x03(\x0b\x32\x0b.proto.Game\x12\x1f\n\nexpansions\x18\r \x03(\x0b\x32\x0b.proto.Game\x12+\n\x0e\x65xternal_games\x18\x0e \x03(\x0b\x32\x13.proto.ExternalGame\x12\x36\n\x12\x66irst_release_date\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07\x66ollows\x18\x10 \x01(\x05\x12#\n\tfranchise\x18\x11 \x01(\x0b\x32\x10.proto.Franchise\x12$\n\nfranchises\x18\x12 \x03(\x0b\x32\x10.proto.Franchise\x12\'\n\x0cgame_engines\x18\x13 \x03(\x0b\x32\x11.proto.GameEngine\x12#\n\ngame_modes\x18\x14 \x03(\x0b\x32\x0f.proto.GameMode\x12\x1c\n\x06genres\x18\x15 \x03(\x0b\x32\x0c.proto.Genre\x12\r\n\x05hypes\x18\x16 \x01(\x05\x12\x32\n\x12involved_companies\x18\x17 \x03(\x0b\x32\x16.proto.InvolvedCompany\x12 \n\x08keywords\x18\x18 \x03(\x0b\x32\x0e.proto.Keyword\x12\x31\n\x11multiplayer_modes\x18\x19 \x03(\x0b\x32\x16.proto.MultiplayerMode\x12\x0c\n\x04name\x18\x1a \x01(\t\x12 \n\x0bparent_game\x18\x1b \x01(\x0b\x32\x0b.proto.Game\x12\"\n\tplatforms\x18\x1c \x03(\x0b\x32\x0f.proto.Platform\x12\x35\n\x13player_perspectives\x18\x1d \x03(\x0b\x32\x18.proto.PlayerPerspective\x12\x0e\n\x06rating\x18\x1e \x01(\x01\x12\x14\n\x0crating_count\x18\x1f \x01(\x05\x12)\n\rrelease_dates\x18  \x03(\x0b\x32\x12.proto.ReleaseDate\x12&\n\x0bscreenshots\x18! \x03(\x0b\x32\x11.proto.Screenshot\x12\"\n\rsimilar_games\x18\" \x03(\x0b\x32\x0b.proto.Game\x12\x0c\n\x04slug\x18# \x01(\t\x12*\n\x15standalone_expansions\x18$ \x03(\x0b\x32\x0b.proto.Game\x12%\n\x06status\x18% \x01(\x0e\x32\x15.proto.GameStatusEnum\x12\x11\n\tstoryline\x18& \x01(\t\x12\x0f\n\x07summary\x18\' \x01(\t\x12\x0c\n\x04tags\x18( \x03(\x05\x12\x1c\n\x06themes\x18) \x03(\x0b\x32\x0c.proto.Theme\x12\x14\n\x0ctotal_rating\x18* \x01(\x01\x12\x1a\n\x12total_rating_count\x18+ \x01(\x05\x12.\n\nupdated_at\x18, \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03url\x18- \x01(\t\x12#\n\x0eversion_parent\x18. \x01(\x0b\x32\x0b.proto.Game\x12\x15\n\rversion_title\x18/ \x01(\t\x12 \n\x06videos\x18\x30 \x03(\x0b\x32\x10.proto.GameVideo\x12 \n\x08websites\x18\x31 \x03(\x0b\x32\x0e.proto.Website\x12\x10\n\x08\x63hecksum\x18\x32 \x01(\t\x12\x1c\n\x07remakes\x18\x33 \x03(\x0b\x32\x0b.proto.Game\x12\x1e\n\tremasters\x18\x34 \x03(\x0b\x32\x0b.proto.Game\x12#\n\x0e\x65xpanded_games\x18\x35 \x03(\x0b\x32\x0b.proto.Game\x12\x1a\n\x05ports\x18\x36 \x03(\x0b\x32\x0b.proto.Game\x12\x1a\n\x05\x66orks\x18\x37 \x03(\x0b\x32\x0b.proto.Game\":\n\x10GameEngineResult\x12&\n\x0bgameengines\x18\x01 \x03(\x0b\x32\x11.proto.GameEngine\"\xb4\x02\n\nGameEngine\x12\n\n\x02id\x18\x01 \x01(\x04\x12!\n\tcompanies\x18\x02 \x03(\x0b\x32\x0e.proto.Company\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12#\n\x04logo\x18\x05 \x01(\x0b\x32\x15.proto.GameEngineLogo\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\"\n\tplatforms\x18\x07 \x03(\x0b\x32\x0f.proto.Platform\x12\x0c\n\x04slug\x18\x08 \x01(\t\x12.\n\nupdated_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03url\x18\n \x01(\t\x12\x10\n\x08\x63hecksum\x18\x0b \x01(\t\"F\n\x14GameEngineLogoResult\x12.\n\x0fgameenginelogos\x18\x01 \x03(\x0b\x32\x15.proto.GameEngineLogo\"\x95\x01\n\x0eGameEngineLogo\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x15\n\ralpha_channel\x18\x02 \x01(\x08\x12\x10\n\x08\x61nimated\x18\x03 \x01(\x08\x12\x0e\n\x06height\x18\x04 \x01(\x05\x12\x10\n\x08image_id\x18\x05 \x01(\t\x12\x0b\n\x03url\x18\x06 \x01(\t\x12\r\n\x05width\x18\x07 \x01(\x05\x12\x10\n\x08\x63hecksum\x18\x08 \x01(\t\"4\n\x0eGameModeResult\x12\"\n\tgamemodes\x18\x01 \x03(\x0b\x32\x0f.proto.GameMode\"\xb1\x01\n\x08GameMode\x12\n\n\x02id\x18\x01 \x01(\x04\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04slug\x18\x04 \x01(\t\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03url\x18\x06 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x07 \x01(\t\"=\n\x11GameVersionResult\x12(\n\x0cgameversions\x18\x01 \x03(\x0b\x32\x12.proto.GameVersion\"\xfc\x01\n\x0bGameVersion\x12\n\n\x02id\x18\x01 \x01(\x04\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x08\x66\x65\x61tures\x18\x03 \x03(\x0b\x32\x19.proto.GameVersionFeature\x12\x19\n\x04game\x18\x04 \x01(\x0b\x32\x0b.proto.Game\x12\x1a\n\x05games\x18\x05 \x03(\x0b\x32\x0b.proto.Game\x12.\n\nupdated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03url\x18\x07 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x08 \x01(\t\"R\n\x18GameVersionFeatureResult\x12\x36\n\x13gameversionfeatures\x18\x01 \x03(\x0b\x32\x19.proto.GameVersionFeature\"\xd1\x01\n\x12GameVersionFeature\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x37\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32%.proto.GameVersionFeatureCategoryEnum\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08position\x18\x04 \x01(\x05\x12\r\n\x05title\x18\x05 \x01(\t\x12.\n\x06values\x18\x06 \x03(\x0b\x32\x1e.proto.GameVersionFeatureValue\x12\x10\n\x08\x63hecksum\x18\x07 \x01(\t\"a\n\x1dGameVersionFeatureValueResult\x12@\n\x18gameversionfeaturevalues\x18\x01 \x03(\x0b\x32\x1e.proto.GameVersionFeatureValue\"\xde\x01\n\x17GameVersionFeatureValue\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x19\n\x04game\x18\x02 \x01(\x0b\x32\x0b.proto.Game\x12/\n\x0cgame_feature\x18\x03 \x01(\x0b\x32\x19.proto.GameVersionFeature\x12K\n\x10included_feature\x18\x04 \x01(\x0e\x32\x31.proto.GameVersionFeatureValueIncludedFeatureEnum\x12\x0c\n\x04note\x18\x05 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x06 \x01(\t\"7\n\x0fGameVideoResult\x12$\n\ngamevideos\x18\x01 \x03(\x0b\x32\x10.proto.GameVideo\"d\n\tGameVideo\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x19\n\x04game\x18\x02 \x01(\x0b\x32\x0b.proto.Game\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08video_id\x18\x04 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x05 \x01(\t\"+\n\x0bGenreResult\x12\x1c\n\x06genres\x18\x01 \x03(\x0b\x32\x0c.proto.Genre\"\xae\x01\n\x05Genre\x12\n\n\x02id\x18\x01 \x01(\x04\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04slug\x18\x04 \x01(\t\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03url\x18\x06 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x07 \x01(\t\"J\n\x15InvolvedCompanyResult\x12\x31\n\x11involvedcompanies\x18\x01 \x03(\x0b\x32\x16.proto.InvolvedCompany\"\x96\x02\n\x0fInvolvedCompany\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x1f\n\x07\x63ompany\x18\x02 \x01(\x0b\x32\x0e.proto.Company\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tdeveloper\x18\x04 \x01(\x08\x12\x19\n\x04game\x18\x05 \x01(\x0b\x32\x0b.proto.Game\x12\x0f\n\x07porting\x18\x06 \x01(\x08\x12\x11\n\tpublisher\x18\x07 \x01(\x08\x12\x12\n\nsupporting\x18\x08 \x01(\x08\x12.\n\nupdated_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08\x63hecksum\x18\n \x01(\t\"1\n\rKeywordResult\x12 \n\x08keywords\x18\x01 \x03(\x0b\x32\x0e.proto.Keyword\"\xb0\x01\n\x07Keyword\x12\n\n\x02id\x18\x01 \x01(\x04\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04slug\x18\x04 \x01(\t\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03url\x18\x06 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x07 \x01(\t\"I\n\x15MultiplayerModeResult\x12\x30\n\x10multiplayermodes\x18\x01 \x03(\x0b\x32\x16.proto.MultiplayerMode\"\xd3\x02\n\x0fMultiplayerMode\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x14\n\x0c\x63\x61mpaigncoop\x18\x02 \x01(\x08\x12\x0e\n\x06\x64ropin\x18\x03 \x01(\x08\x12\x19\n\x04game\x18\x04 \x01(\x0b\x32\x0b.proto.Game\x12\x0f\n\x07lancoop\x18\x05 \x01(\x08\x12\x13\n\x0bofflinecoop\x18\x06 \x01(\x08\x12\x16\n\x0eofflinecoopmax\x18\x07 \x01(\x05\x12\x12\n\nofflinemax\x18\x08 \x01(\x05\x12\x12\n\nonlinecoop\x18\t \x01(\x08\x12\x15\n\ronlinecoopmax\x18\n \x01(\x05\x12\x11\n\tonlinemax\x18\x0b \x01(\x05\x12!\n\x08platform\x18\x0c \x01(\x0b\x32\x0f.proto.Platform\x12\x13\n\x0bsplitscreen\x18\r \x01(\x08\x12\x19\n\x11splitscreenonline\x18\x0e \x01(\x08\x12\x10\n\x08\x63hecksum\x18\x0f \x01(\t\"4\n\x0ePlatformResult\x12\"\n\tplatforms\x18\x01 \x03(\x0b\x32\x0f.proto.Platform\"\xe5\x03\n\x08Platform\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x14\n\x0c\x61\x62\x62reviation\x18\x02 \x01(\t\x12\x18\n\x10\x61lternative_name\x18\x03 \x01(\t\x12-\n\x08\x63\x61tegory\x18\x04 \x01(\x0e\x32\x1b.proto.PlatformCategoryEnum\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\ngeneration\x18\x06 \x01(\x05\x12\x0c\n\x04name\x18\x07 \x01(\t\x12*\n\rplatform_logo\x18\x08 \x01(\x0b\x32\x13.proto.PlatformLogo\x12.\n\x0fplatform_family\x18\t \x01(\x0b\x32\x15.proto.PlatformFamily\x12\x0c\n\x04slug\x18\n \x01(\t\x12\x0f\n\x07summary\x18\x0b \x01(\t\x12.\n\nupdated_at\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03url\x18\r \x01(\t\x12(\n\x08versions\x18\x0e \x03(\x0b\x32\x16.proto.PlatformVersion\x12(\n\x08websites\x18\x0f \x03(\x0b\x32\x16.proto.PlatformWebsite\x12\x10\n\x08\x63hecksum\x18\x10 \x01(\t\"G\n\x14PlatformFamilyResult\x12/\n\x10platformfamilies\x18\x01 \x03(\x0b\x32\x15.proto.PlatformFamily\"J\n\x0ePlatformFamily\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04slug\x18\x03 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x04 \x01(\t\"@\n\x12PlatformLogoResult\x12*\n\rplatformlogos\x18\x01 \x03(\x0b\x32\x13.proto.PlatformLogo\"\x93\x01\n\x0cPlatformLogo\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x15\n\ralpha_channel\x18\x02 \x01(\x08\x12\x10\n\x08\x61nimated\x18\x03 \x01(\x08\x12\x0e\n\x06height\x18\x04 \x01(\x05\x12\x10\n\x08image_id\x18\x05 \x01(\t\x12\x0b\n\x03url\x18\x06 \x01(\t\x12\r\n\x05width\x18\x07 \x01(\x05\x12\x10\n\x08\x63hecksum\x18\x08 \x01(\t\"I\n\x15PlatformVersionResult\x12\x30\n\x10platformversions\x18\x01 \x03(\x0b\x32\x16.proto.PlatformVersion\"\x81\x04\n\x0fPlatformVersion\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x30\n\tcompanies\x18\x02 \x03(\x0b\x32\x1d.proto.PlatformVersionCompany\x12\x14\n\x0c\x63onnectivity\x18\x03 \x01(\t\x12\x0b\n\x03\x63pu\x18\x04 \x01(\t\x12\x10\n\x08graphics\x18\x05 \x01(\t\x12\x38\n\x11main_manufacturer\x18\x06 \x01(\x0b\x32\x1d.proto.PlatformVersionCompany\x12\r\n\x05media\x18\x07 \x01(\t\x12\x0e\n\x06memory\x18\x08 \x01(\t\x12\x0c\n\x04name\x18\t \x01(\t\x12\x0e\n\x06online\x18\n \x01(\t\x12\n\n\x02os\x18\x0b \x01(\t\x12\x0e\n\x06output\x18\x0c \x01(\t\x12*\n\rplatform_logo\x18\r \x01(\x0b\x32\x13.proto.PlatformLogo\x12I\n\x1eplatform_version_release_dates\x18\x0e \x03(\x0b\x32!.proto.PlatformVersionReleaseDate\x12\x13\n\x0bresolutions\x18\x0f \x01(\t\x12\x0c\n\x04slug\x18\x10 \x01(\t\x12\r\n\x05sound\x18\x11 \x01(\t\x12\x0f\n\x07storage\x18\x12 \x01(\t\x12\x0f\n\x07summary\x18\x13 \x01(\t\x12\x0b\n\x03url\x18\x14 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x15 \x01(\t\"_\n\x1cPlatformVersionCompanyResult\x12?\n\x18platformversioncompanies\x18\x01 \x03(\x0b\x32\x1d.proto.PlatformVersionCompany\"\x91\x01\n\x16PlatformVersionCompany\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x12\x1f\n\x07\x63ompany\x18\x03 \x01(\x0b\x32\x0e.proto.Company\x12\x11\n\tdeveloper\x18\x04 \x01(\x08\x12\x14\n\x0cmanufacturer\x18\x05 \x01(\x08\x12\x10\n\x08\x63hecksum\x18\x06 \x01(\t\"j\n PlatformVersionReleaseDateResult\x12\x46\n\x1bplatformversionreleasedates\x18\x01 \x03(\x0b\x32!.proto.PlatformVersionReleaseDate\"\xff\x02\n\x1aPlatformVersionReleaseDate\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x39\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\'.proto.DateFormatChangeDateCategoryEnum\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x04\x64\x61te\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05human\x18\x05 \x01(\t\x12\t\n\x01m\x18\x06 \x01(\x05\x12\x30\n\x10platform_version\x18\x07 \x01(\x0b\x32\x16.proto.PlatformVersion\x12\'\n\x06region\x18\x08 \x01(\x0e\x32\x17.proto.RegionRegionEnum\x12.\n\nupdated_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\t\n\x01y\x18\n \x01(\x05\x12\x10\n\x08\x63hecksum\x18\x0b \x01(\t\"I\n\x15PlatformWebsiteResult\x12\x30\n\x10platformwebsites\x18\x01 \x03(\x0b\x32\x16.proto.PlatformWebsite\"{\n\x0fPlatformWebsite\x12\n\n\x02id\x18\x01 \x01(\x04\x12,\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\x1a.proto.WebsiteCategoryEnum\x12\x0f\n\x07trusted\x18\x03 \x01(\x08\x12\x0b\n\x03url\x18\x04 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x05 \x01(\t\"O\n\x17PlayerPerspectiveResult\x12\x34\n\x12playerperspectives\x18\x01 \x03(\x0b\x32\x18.proto.PlayerPerspective\"\xba\x01\n\x11PlayerPerspective\x12\n\n\x02id\x18\x01 \x01(\x04\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04slug\x18\x04 \x01(\t\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03url\x18\x06 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x07 \x01(\t\"=\n\x11ReleaseDateResult\x12(\n\x0creleasedates\x18\x01 \x03(\x0b\x32\x12.proto.ReleaseDate\"\xfc\x02\n\x0bReleaseDate\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x39\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\'.proto.DateFormatChangeDateCategoryEnum\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x04\x64\x61te\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x19\n\x04game\x18\x05 \x01(\x0b\x32\x0b.proto.Game\x12\r\n\x05human\x18\x06 \x01(\t\x12\t\n\x01m\x18\x07 \x01(\x05\x12!\n\x08platform\x18\x08 \x01(\x0b\x32\x0f.proto.Platform\x12\'\n\x06region\x18\t \x01(\x0e\x32\x17.proto.RegionRegionEnum\x12.\n\nupdated_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\t\n\x01y\x18\x0b \x01(\x05\x12\x10\n\x08\x63hecksum\x18\x0c \x01(\t\":\n\x10ScreenshotResult\x12&\n\x0bscreenshots\x18\x01 \x03(\x0b\x32\x11.proto.Screenshot\"\xac\x01\n\nScreenshot\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x15\n\ralpha_channel\x18\x02 \x01(\x08\x12\x10\n\x08\x61nimated\x18\x03 \x01(\x08\x12\x19\n\x04game\x18\x04 \x01(\x0b\x32\x0b.proto.Game\x12\x0e\n\x06height\x18\x05 \x01(\x05\x12\x10\n\x08image_id\x18\x06 \x01(\t\x12\x0b\n\x03url\x18\x07 \x01(\t\x12\r\n\x05width\x18\x08 \x01(\x05\x12\x10\n\x08\x63hecksum\x18\t \x01(\t\"/\n\x0cSearchResult\x12\x1f\n\x08searches\x18\x01 \x03(\x0b\x32\r.proto.Search\"\x83\x03\n\x06Search\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x18\n\x10\x61lternative_name\x18\x02 \x01(\t\x12#\n\tcharacter\x18\x03 \x01(\x0b\x32\x10.proto.Character\x12%\n\ncollection\x18\x04 \x01(\x0b\x32\x11.proto.Collection\x12\x1f\n\x07\x63ompany\x18\x05 \x01(\x0b\x32\x0e.proto.Company\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x19\n\x04game\x18\x07 \x01(\x0b\x32\x0b.proto.Game\x12\x0c\n\x04name\x18\x08 \x01(\t\x12!\n\x08platform\x18\t \x01(\x0b\x32\x0f.proto.Platform\x12\x30\n\x0cpublished_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12$\n\ntest_dummy\x18\x0b \x01(\x0b\x32\x10.proto.TestDummy\x12\x1b\n\x05theme\x18\x0c \x01(\x0b\x32\x0c.proto.Theme\x12\x10\n\x08\x63hecksum\x18\r \x01(\t\"8\n\x0fTestDummyResult\x12%\n\x0btestdummies\x18\x01 \x03(\x0b\x32\x10.proto.TestDummy\"\xe5\x03\n\tTestDummy\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x12\n\nbool_value\x18\x02 \x01(\x08\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\tenum_test\x18\x04 \x01(\x0e\x32\x1c.proto.TestDummyEnumTestEnum\x12\x13\n\x0b\x66loat_value\x18\x05 \x01(\x01\x12\x19\n\x04game\x18\x06 \x01(\x0b\x32\x0b.proto.Game\x12\x15\n\rinteger_array\x18\x07 \x03(\x05\x12\x15\n\rinteger_value\x18\x08 \x01(\x05\x12\x0c\n\x04name\x18\t \x01(\t\x12\x19\n\x11new_integer_value\x18\n \x01(\x05\x12\x0f\n\x07private\x18\x0b \x01(\x08\x12\x0c\n\x04slug\x18\x0c \x01(\t\x12\x14\n\x0cstring_array\x18\r \x03(\t\x12&\n\x0ctest_dummies\x18\x0e \x03(\x0b\x32\x10.proto.TestDummy\x12$\n\ntest_dummy\x18\x0f \x01(\x0b\x32\x10.proto.TestDummy\x12.\n\nupdated_at\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03url\x18\x11 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x12 \x01(\t\"+\n\x0bThemeResult\x12\x1c\n\x06themes\x18\x01 \x03(\x0b\x32\x0c.proto.Theme\"\xae\x01\n\x05Theme\x12\n\n\x02id\x18\x01 \x01(\x04\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04slug\x18\x04 \x01(\t\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03url\x18\x06 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x07 \x01(\t\"1\n\rWebsiteResult\x12 \n\x08websites\x18\x01 \x03(\x0b\x32\x0e.proto.Website\"\x8e\x01\n\x07Website\x12\n\n\x02id\x18\x01 \x01(\x04\x12,\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\x1a.proto.WebsiteCategoryEnum\x12\x19\n\x04game\x18\x03 \x01(\x0b\x32\x0b.proto.Game\x12\x0f\n\x07trusted\x18\x04 \x01(\x08\x12\x0b\n\x03url\x18\x05 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x06 \x01(\t*}\n\x15\x41geRatingCategoryEnum\x12\x1b\n\x17\x41GERATING_CATEGORY_NULL\x10\x00\x12\x08\n\x04\x45SRB\x10\x01\x12\x08\n\x04PEGI\x10\x02\x12\x08\n\x04\x43\x45RO\x10\x03\x12\x07\n\x03USK\x10\x04\x12\x08\n\x04GRAC\x10\x05\x12\r\n\tCLASS_IND\x10\x06\x12\x07\n\x03\x41\x43\x42\x10\x07*\xad\x04\n\x13\x41geRatingRatingEnum\x12\x19\n\x15\x41GERATING_RATING_NULL\x10\x00\x12\t\n\x05THREE\x10\x01\x12\t\n\x05SEVEN\x10\x02\x12\n\n\x06TWELVE\x10\x03\x12\x0b\n\x07SIXTEEN\x10\x04\x12\x0c\n\x08\x45IGHTEEN\x10\x05\x12\x06\n\x02RP\x10\x06\x12\x06\n\x02\x45\x43\x10\x07\x12\x05\n\x01\x45\x10\x08\x12\x07\n\x03\x45\x31\x30\x10\t\x12\x05\n\x01T\x10\n\x12\x05\n\x01M\x10\x0b\x12\x06\n\x02\x41O\x10\x0c\x12\n\n\x06\x43\x45RO_A\x10\r\x12\n\n\x06\x43\x45RO_B\x10\x0e\x12\n\n\x06\x43\x45RO_C\x10\x0f\x12\n\n\x06\x43\x45RO_D\x10\x10\x12\n\n\x06\x43\x45RO_Z\x10\x11\x12\t\n\x05USK_0\x10\x12\x12\t\n\x05USK_6\x10\x13\x12\n\n\x06USK_12\x10\x14\x12\n\n\x06USK_18\x10\x15\x12\x0c\n\x08GRAC_ALL\x10\x16\x12\x0f\n\x0bGRAC_TWELVE\x10\x17\x12\x10\n\x0cGRAC_FIFTEEN\x10\x18\x12\x11\n\rGRAC_EIGHTEEN\x10\x19\x12\x10\n\x0cGRAC_TESTING\x10\x1a\x12\x0f\n\x0b\x43LASS_IND_L\x10\x1b\x12\x11\n\rCLASS_IND_TEN\x10\x1c\x12\x14\n\x10\x43LASS_IND_TWELVE\x10\x1d\x12\x16\n\x12\x43LASS_IND_FOURTEEN\x10\x1e\x12\x15\n\x11\x43LASS_IND_SIXTEEN\x10\x1f\x12\x16\n\x12\x43LASS_IND_EIGHTEEN\x10 \x12\t\n\x05\x41\x43\x42_G\x10!\x12\n\n\x06\x41\x43\x42_PG\x10\"\x12\t\n\x05\x41\x43\x42_M\x10#\x12\x0c\n\x08\x41\x43\x42_MA15\x10$\x12\x0b\n\x07\x41\x43\x42_R18\x10%\x12\n\n\x06\x41\x43\x42_RC\x10&*3\n\x10GenderGenderEnum\x12\x08\n\x04MALE\x10\x00\x12\n\n\x06\x46\x45MALE\x10\x01\x12\t\n\x05OTHER\x10\x02*n\n\x14\x43haracterSpeciesEnum\x12\x1a\n\x16\x43HARACTER_SPECIES_NULL\x10\x00\x12\t\n\x05HUMAN\x10\x01\x12\t\n\x05\x41LIEN\x10\x02\x12\n\n\x06\x41NIMAL\x10\x03\x12\x0b\n\x07\x41NDROID\x10\x04\x12\x0b\n\x07UNKNOWN\x10\x05*\x83\x01\n DateFormatChangeDateCategoryEnum\x12\x0e\n\nYYYYMMMMDD\x10\x00\x12\x0c\n\x08YYYYMMMM\x10\x01\x12\x08\n\x04YYYY\x10\x02\x12\n\n\x06YYYYQ1\x10\x03\x12\n\n\x06YYYYQ2\x10\x04\x12\n\n\x06YYYYQ3\x10\x05\x12\n\n\x06YYYYQ4\x10\x06\x12\x07\n\x03TBD\x10\x07*\x8c\x03\n\x13WebsiteCategoryEnum\x12\x19\n\x15WEBSITE_CATEGORY_NULL\x10\x00\x12\x14\n\x10WEBSITE_OFFICIAL\x10\x01\x12\x11\n\rWEBSITE_WIKIA\x10\x02\x12\x15\n\x11WEBSITE_WIKIPEDIA\x10\x03\x12\x14\n\x10WEBSITE_FACEBOOK\x10\x04\x12\x13\n\x0fWEBSITE_TWITTER\x10\x05\x12\x12\n\x0eWEBSITE_TWITCH\x10\x06\x12\x15\n\x11WEBSITE_INSTAGRAM\x10\x08\x12\x13\n\x0fWEBSITE_YOUTUBE\x10\t\x12\x12\n\x0eWEBSITE_IPHONE\x10\n\x12\x10\n\x0cWEBSITE_IPAD\x10\x0b\x12\x13\n\x0fWEBSITE_ANDROID\x10\x0c\x12\x11\n\rWEBSITE_STEAM\x10\r\x12\x12\n\x0eWEBSITE_REDDIT\x10\x0e\x12\x10\n\x0cWEBSITE_ITCH\x10\x0f\x12\x15\n\x11WEBSITE_EPICGAMES\x10\x10\x12\x0f\n\x0bWEBSITE_GOG\x10\x11\x12\x13\n\x0fWEBSITE_DISCORD\x10\x12*\xfd\x02\n\x18\x45xternalGameCategoryEnum\x12\x1e\n\x1a\x45XTERNALGAME_CATEGORY_NULL\x10\x00\x12\x16\n\x12\x45XTERNALGAME_STEAM\x10\x01\x12\x14\n\x10\x45XTERNALGAME_GOG\x10\x05\x12\x18\n\x14\x45XTERNALGAME_YOUTUBE\x10\n\x12\x1a\n\x16\x45XTERNALGAME_MICROSOFT\x10\x0b\x12\x16\n\x12\x45XTERNALGAME_APPLE\x10\r\x12\x17\n\x13\x45XTERNALGAME_TWITCH\x10\x0e\x12\x18\n\x14\x45XTERNALGAME_ANDROID\x10\x0f\x12\x1c\n\x18\x45XTERNALGAME_AMAZON_ASIN\x10\x14\x12\x1c\n\x18\x45XTERNALGAME_AMAZON_LUNA\x10\x16\x12\x1b\n\x17\x45XTERNALGAME_AMAZON_ADG\x10\x17\x12 \n\x1c\x45XTERNALGAME_EPIC_GAME_STORE\x10\x1a\x12\x17\n\x13\x45XTERNALGAME_OCULUS\x10\x1c*i\n\x15\x45xternalGameMediaEnum\x12\x1b\n\x17\x45XTERNALGAME_MEDIA_NULL\x10\x00\x12\x18\n\x14\x45XTERNALGAME_DIGITAL\x10\x01\x12\x19\n\x15\x45XTERNALGAME_PHYSICAL\x10\x02*\xc8\x01\n\x10GameCategoryEnum\x12\r\n\tMAIN_GAME\x10\x00\x12\r\n\tDLC_ADDON\x10\x01\x12\r\n\tEXPANSION\x10\x02\x12\n\n\x06\x42UNDLE\x10\x03\x12\x18\n\x14STANDALONE_EXPANSION\x10\x04\x12\x07\n\x03MOD\x10\x05\x12\x0b\n\x07\x45PISODE\x10\x06\x12\n\n\x06SEASON\x10\x07\x12\n\n\x06REMAKE\x10\x08\x12\x0c\n\x08REMASTER\x10\t\x12\x11\n\rEXPANDED_GAME\x10\n\x12\x08\n\x04PORT\x10\x0b\x12\x08\n\x04\x46ORK\x10\x0c*|\n\x0eGameStatusEnum\x12\x0c\n\x08RELEASED\x10\x00\x12\t\n\x05\x41LPHA\x10\x02\x12\x08\n\x04\x42\x45TA\x10\x03\x12\x10\n\x0c\x45\x41RLY_ACCESS\x10\x04\x12\x0b\n\x07OFFLINE\x10\x05\x12\r\n\tCANCELLED\x10\x06\x12\x0b\n\x07RUMORED\x10\x07\x12\x0c\n\x08\x44\x45LISTED\x10\x08*>\n\x1eGameVersionFeatureCategoryEnum\x12\x0b\n\x07\x42OOLEAN\x10\x00\x12\x0f\n\x0b\x44\x45SCRIPTION\x10\x01*`\n*GameVersionFeatureValueIncludedFeatureEnum\x12\x10\n\x0cNOT_INCLUDED\x10\x00\x12\x0c\n\x08INCLUDED\x10\x01\x12\x12\n\x0ePRE_ORDER_ONLY\x10\x02*\x93\x01\n\x14PlatformCategoryEnum\x12\x1a\n\x16PLATFORM_CATEGORY_NULL\x10\x00\x12\x0b\n\x07\x43ONSOLE\x10\x01\x12\n\n\x06\x41RCADE\x10\x02\x12\x0c\n\x08PLATFORM\x10\x03\x12\x14\n\x10OPERATING_SYSTEM\x10\x04\x12\x14\n\x10PORTABLE_CONSOLE\x10\x05\x12\x0c\n\x08\x43OMPUTER\x10\x06*\xaf\x01\n\x10RegionRegionEnum\x12\x16\n\x12REGION_REGION_NULL\x10\x00\x12\n\n\x06\x45UROPE\x10\x01\x12\x11\n\rNORTH_AMERICA\x10\x02\x12\r\n\tAUSTRALIA\x10\x03\x12\x0f\n\x0bNEW_ZEALAND\x10\x04\x12\t\n\x05JAPAN\x10\x05\x12\t\n\x05\x43HINA\x10\x06\x12\x08\n\x04\x41SIA\x10\x07\x12\r\n\tWORLDWIDE\x10\x08\x12\t\n\x05KOREA\x10\t\x12\n\n\x06\x42RAZIL\x10\n*K\n\x15TestDummyEnumTestEnum\x12\x1c\n\x18TESTDUMMY_ENUM_TEST_NULL\x10\x00\x12\t\n\x05\x45NUM1\x10\x01\x12\t\n\x05\x45NUM2\x10\x02\x42\x04H\x02P\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'igdbapi_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\002P\001'
  _AGERATINGCATEGORYENUM._serialized_start=13943
  _AGERATINGCATEGORYENUM._serialized_end=14068
  _AGERATINGRATINGENUM._serialized_start=14071
  _AGERATINGRATINGENUM._serialized_end=14628
  _GENDERGENDERENUM._serialized_start=14630
  _GENDERGENDERENUM._serialized_end=14681
  _CHARACTERSPECIESENUM._serialized_start=14683
  _CHARACTERSPECIESENUM._serialized_end=14793
  _DATEFORMATCHANGEDATECATEGORYENUM._serialized_start=14796
  _DATEFORMATCHANGEDATECATEGORYENUM._serialized_end=14927
  _WEBSITECATEGORYENUM._serialized_start=14930
  _WEBSITECATEGORYENUM._serialized_end=15326
  _EXTERNALGAMECATEGORYENUM._serialized_start=15329
  _EXTERNALGAMECATEGORYENUM._serialized_end=15710
  _EXTERNALGAMEMEDIAENUM._serialized_start=15712
  _EXTERNALGAMEMEDIAENUM._serialized_end=15817
  _GAMECATEGORYENUM._serialized_start=15820
  _GAMECATEGORYENUM._serialized_end=16020
  _GAMESTATUSENUM._serialized_start=16022
  _GAMESTATUSENUM._serialized_end=16146
  _GAMEVERSIONFEATURECATEGORYENUM._serialized_start=16148
  _GAMEVERSIONFEATURECATEGORYENUM._serialized_end=16210
  _GAMEVERSIONFEATUREVALUEINCLUDEDFEATUREENUM._serialized_start=16212
  _GAMEVERSIONFEATUREVALUEINCLUDEDFEATUREENUM._serialized_end=16308
  _PLATFORMCATEGORYENUM._serialized_start=16311
  _PLATFORMCATEGORYENUM._serialized_end=16458
  _REGIONREGIONENUM._serialized_start=16461
  _REGIONREGIONENUM._serialized_end=16636
  _TESTDUMMYENUMTESTENUM._serialized_start=16638
  _TESTDUMMYENUMTESTENUM._serialized_end=16713
  _COUNT._serialized_start=57
  _COUNT._serialized_end=79
  _MULTIQUERYRESULT._serialized_start=81
  _MULTIQUERYRESULT._serialized_end=145
  _MULTIQUERYRESULTARRAY._serialized_start=147
  _MULTIQUERYRESULTARRAY._serialized_end=211
  _AGERATINGRESULT._serialized_start=213
  _AGERATINGRESULT._serialized_end=268
  _AGERATING._serialized_start=271
  _AGERATING._serialized_end=514
  _AGERATINGCONTENTDESCRIPTIONRESULT._serialized_start=516
  _AGERATINGCONTENTDESCRIPTIONRESULT._serialized_end=625
  _AGERATINGCONTENTDESCRIPTION._serialized_start=627
  _AGERATINGCONTENTDESCRIPTION._serialized_end=753
  _ALTERNATIVENAMERESULT._serialized_start=755
  _ALTERNATIVENAMERESULT._serialized_end=828
  _ALTERNATIVENAME._serialized_start=830
  _ALTERNATIVENAME._serialized_end=935
  _ARTWORKRESULT._serialized_start=937
  _ARTWORKRESULT._serialized_end=986
  _ARTWORK._serialized_start=989
  _ARTWORK._serialized_end=1158
  _CHARACTERRESULT._serialized_start=1160
  _CHARACTERRESULT._serialized_end=1215
  _CHARACTER._serialized_start=1218
  _CHARACTER._serialized_end=1611
  _CHARACTERMUGSHOTRESULT._serialized_start=1613
  _CHARACTERMUGSHOTRESULT._serialized_end=1689
  _CHARACTERMUGSHOT._serialized_start=1692
  _CHARACTERMUGSHOT._serialized_end=1843
  _COLLECTIONRESULT._serialized_start=1845
  _COLLECTIONRESULT._serialized_end=1903
  _COLLECTION._serialized_start=1906
  _COLLECTION._serialized_end=2113
  _COMPANYRESULT._serialized_start=2115
  _COMPANYRESULT._serialized_end=2165
  _COMPANY._serialized_start=2168
  _COMPANY._serialized_end=2835
  _COMPANYLOGORESULT._serialized_start=2837
  _COMPANYLOGORESULT._serialized_end=2898
  _COMPANYLOGO._serialized_start=2901
  _COMPANYLOGO._serialized_end=3047
  _COMPANYWEBSITERESULT._serialized_start=3049
  _COMPANYWEBSITERESULT._serialized_end=3119
  _COMPANYWEBSITE._serialized_start=3121
  _COMPANYWEBSITE._serialized_end=3243
  _COVERRESULT._serialized_start=3245
  _COVERRESULT._serialized_end=3288
  _COVER._serialized_start=3291
  _COVER._serialized_end=3458
  _EXTERNALGAMERESULT._serialized_start=3460
  _EXTERNALGAMERESULT._serialized_end=3524
  _EXTERNALGAME._serialized_start=3527
  _EXTERNALGAME._serialized_end=3898
  _FRANCHISERESULT._serialized_start=3900
  _FRANCHISERESULT._serialized_end=3955
  _FRANCHISE._serialized_start=3958
  _FRANCHISE._serialized_end=4164
  _GAMERESULT._serialized_start=4166
  _GAMERESULT._serialized_end=4206
  _GAME._serialized_start=4209
  _GAME._serialized_end=5998
  _GAMEENGINERESULT._serialized_start=6000
  _GAMEENGINERESULT._serialized_end=6058
  _GAMEENGINE._serialized_start=6061
  _GAMEENGINE._serialized_end=6369
  _GAMEENGINELOGORESULT._serialized_start=6371
  _GAMEENGINELOGORESULT._serialized_end=6441
  _GAMEENGINELOGO._serialized_start=6444
  _GAMEENGINELOGO._serialized_end=6593
  _GAMEMODERESULT._serialized_start=6595
  _GAMEMODERESULT._serialized_end=6647
  _GAMEMODE._serialized_start=6650
  _GAMEMODE._serialized_end=6827
  _GAMEVERSIONRESULT._serialized_start=6829
  _GAMEVERSIONRESULT._serialized_end=6890
  _GAMEVERSION._serialized_start=6893
  _GAMEVERSION._serialized_end=7145
  _GAMEVERSIONFEATURERESULT._serialized_start=7147
  _GAMEVERSIONFEATURERESULT._serialized_end=7229
  _GAMEVERSIONFEATURE._serialized_start=7232
  _GAMEVERSIONFEATURE._serialized_end=7441
  _GAMEVERSIONFEATUREVALUERESULT._serialized_start=7443
  _GAMEVERSIONFEATUREVALUERESULT._serialized_end=7540
  _GAMEVERSIONFEATUREVALUE._serialized_start=7543
  _GAMEVERSIONFEATUREVALUE._serialized_end=7765
  _GAMEVIDEORESULT._serialized_start=7767
  _GAMEVIDEORESULT._serialized_end=7822
  _GAMEVIDEO._serialized_start=7824
  _GAMEVIDEO._serialized_end=7924
  _GENRERESULT._serialized_start=7926
  _GENRERESULT._serialized_end=7969
  _GENRE._serialized_start=7972
  _GENRE._serialized_end=8146
  _INVOLVEDCOMPANYRESULT._serialized_start=8148
  _INVOLVEDCOMPANYRESULT._serialized_end=8222
  _INVOLVEDCOMPANY._serialized_start=8225
  _INVOLVEDCOMPANY._serialized_end=8503
  _KEYWORDRESULT._serialized_start=8505
  _KEYWORDRESULT._serialized_end=8554
  _KEYWORD._serialized_start=8557
  _KEYWORD._serialized_end=8733
  _MULTIPLAYERMODERESULT._serialized_start=8735
  _MULTIPLAYERMODERESULT._serialized_end=8808
  _MULTIPLAYERMODE._serialized_start=8811
  _MULTIPLAYERMODE._serialized_end=9150
  _PLATFORMRESULT._serialized_start=9152
  _PLATFORMRESULT._serialized_end=9204
  _PLATFORM._serialized_start=9207
  _PLATFORM._serialized_end=9692
  _PLATFORMFAMILYRESULT._serialized_start=9694
  _PLATFORMFAMILYRESULT._serialized_end=9765
  _PLATFORMFAMILY._serialized_start=9767
  _PLATFORMFAMILY._serialized_end=9841
  _PLATFORMLOGORESULT._serialized_start=9843
  _PLATFORMLOGORESULT._serialized_end=9907
  _PLATFORMLOGO._serialized_start=9910
  _PLATFORMLOGO._serialized_end=10057
  _PLATFORMVERSIONRESULT._serialized_start=10059
  _PLATFORMVERSIONRESULT._serialized_end=10132
  _PLATFORMVERSION._serialized_start=10135
  _PLATFORMVERSION._serialized_end=10648
  _PLATFORMVERSIONCOMPANYRESULT._serialized_start=10650
  _PLATFORMVERSIONCOMPANYRESULT._serialized_end=10745
  _PLATFORMVERSIONCOMPANY._serialized_start=10748
  _PLATFORMVERSIONCOMPANY._serialized_end=10893
  _PLATFORMVERSIONRELEASEDATERESULT._serialized_start=10895
  _PLATFORMVERSIONRELEASEDATERESULT._serialized_end=11001
  _PLATFORMVERSIONRELEASEDATE._serialized_start=11004
  _PLATFORMVERSIONRELEASEDATE._serialized_end=11387
  _PLATFORMWEBSITERESULT._serialized_start=11389
  _PLATFORMWEBSITERESULT._serialized_end=11462
  _PLATFORMWEBSITE._serialized_start=11464
  _PLATFORMWEBSITE._serialized_end=11587
  _PLAYERPERSPECTIVERESULT._serialized_start=11589
  _PLAYERPERSPECTIVERESULT._serialized_end=11668
  _PLAYERPERSPECTIVE._serialized_start=11671
  _PLAYERPERSPECTIVE._serialized_end=11857
  _RELEASEDATERESULT._serialized_start=11859
  _RELEASEDATERESULT._serialized_end=11920
  _RELEASEDATE._serialized_start=11923
  _RELEASEDATE._serialized_end=12303
  _SCREENSHOTRESULT._serialized_start=12305
  _SCREENSHOTRESULT._serialized_end=12363
  _SCREENSHOT._serialized_start=12366
  _SCREENSHOT._serialized_end=12538
  _SEARCHRESULT._serialized_start=12540
  _SEARCHRESULT._serialized_end=12587
  _SEARCH._serialized_start=12590
  _SEARCH._serialized_end=12977
  _TESTDUMMYRESULT._serialized_start=12979
  _TESTDUMMYRESULT._serialized_end=13035
  _TESTDUMMY._serialized_start=13038
  _TESTDUMMY._serialized_end=13523
  _THEMERESULT._serialized_start=13525
  _THEMERESULT._serialized_end=13568
  _THEME._serialized_start=13571
  _THEME._serialized_end=13745
  _WEBSITERESULT._serialized_start=13747
  _WEBSITERESULT._serialized_end=13796
  _WEBSITE._serialized_start=13799
  _WEBSITE._serialized_end=13941
# @@protoc_insertion_point(module_scope)